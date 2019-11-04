'''
Created on 21.02.2014

@author: bm1281
'''

from xml.etree import ElementTree as ET
import arcpy

# format the cooridnates to floats with desired number of decimals
def formatPositionFloats(posListString, decimalsNumber):
    posListMembers = posListString.split(" ")
    
    posList = ""
    
    for posListMember in posListMembers:
        posFloat = float(posListMember)
        posFloat = format(posFloat,'.' + str(decimalsNumber) + 'f')
        posList = posList + str(posFloat) + " "
    
    posList = posList.strip()
    
    return posList

# get the value of srsName attribute like http://www.opengis.net/gml/srs/epsg.xml#4326
# with epsg of feature class
def getEPSG(featureCollection):
    srs   = arcpy.Describe(featureCollection).spatialReference
    
    # Get EPSG for srsName attribute of geometry elements
    srsAttributeText = ""
    srsType = srs.type
    
    if srsType == "Geographic":
        srsAttributeText = "http://www.opengis.net/gml/srs/epsg.xml#" + str(srs.GCSCode)
    elif srsType =="Projected":
        srsAttributeText = "http://www.opengis.net/gml/srs/epsg.xml#" + str(srs.PCSCode)
    else:
        srsAttributeText = "http://www.opengis.net/gml/srs/epsg.xml#4326"
    
    return srsAttributeText


# convert wkt string from arcpy.geom.WKT to gml element
def convertWktToGml(wktGeomString):
    
    ET.register_namespace("gml" , "http://www.opengis.net/gml/3.2")
    
    wktGeomString = str(wktGeomString).strip()
    
    geomElementList = []
    
#---------------------------------------------------------------------------------------------------
# POINTS and MULTIPOINTS
#---------------------------------------------------------------------------------------------------
    if wktGeomString.startswith("POINT") or wktGeomString.startswith("MULTIPOINT"):
        pointElementList = []
        pointString = wktGeomString[wktGeomString.find("("):]      \
                                                 .strip()          \
                                                 .replace(" " ,",")\
                                                 .replace(",,",",")
                                                 
        pointStringList = pointString.split("),(")
        
        for pointStr in pointStringList:
            pointElement = ET.Element("{http://www.opengis.net/gml/3.2}Point")
            pointElement.attrib["srsName"] = "http://www.opengis.net/gml/srs/epsg.xml#4326"
            
            pointStr = pointStr.replace("((","") \
                               .replace("))","") \
                               .replace("(" ,"") \
                               .replace(")" ,"") \
                               .replace("," ," ")\
                               .strip()
                               
            # Get each pos (lat lon) to convert to float with 3 decimals
            pointStr = formatPositionFloats(pointStr, 3)
            
            posElement = ET.SubElement(pointElement, "{http://www.opengis.net/gml/3.2}pos")
            posElement.text = pointStr
            pointElementList.append(pointElement)
        geomElementList = pointElementList
            
#--------------------------------------------------------------------------------------------------
# LINESTRINGS and MULTILINESTRINGS
#--------------------------------------------------------------------------------------------------       
    if wktGeomString.startswith("LINESTRING") or wktGeomString.startswith("MULTILINESTRING"):
        lineElementList = []
        lineString = wktGeomString[wktGeomString.find("("):]        \
                                                .strip()            \
                                                .replace(" " , ",")  \
                                                .replace(",,", ",")
        
        lineStringList = lineString.split("),(")
        
        for lineStr in lineStringList:
            
            lineStringElement = ET.Element("{http://www.opengis.net/gml/3.2}LineString")
            lineStringElement.attrib["srsName"] = "http://www.opengis.net/gml/srs/epsg.xml#4326"
            
            lineStr = lineStr.replace("((","") \
                             .replace("))","") \
                             .replace("(" ,"") \
                             .replace(")" ,"") \
                             .replace("," ," ")\
                             .strip()
            
            # Get each pos (lat lon) to convert to float with 3 decimals
            lineStr = formatPositionFloats(lineStr, 3)
            
            posListElement = ET.SubElement(lineStringElement, "{http://www.opengis.net/gml/3.2}posList")
            posListElement.text = lineStr
            lineElementList.append(lineStringElement)
        geomElementList = lineElementList

#---------------------------------------------------------------------------------------------------
# POLYGONS and MULTIPOLYGONS
#---------------------------------------------------------------------------------------------------
    if wktGeomString.startswith("POLYGON") or wktGeomString.startswith("MULTIPOLYGON"):
        polygonElementList = []
        polygonString = wktGeomString[wktGeomString.find("(("):]     \
                                                   .strip()          \
                                                   .replace(" ", ",")\
                                                   .replace(",,",",")
        
        polygonStringList = polygonString.split(")),((")
        
        for polString in polygonStringList:
            polygonElement = ET.Element("{http://www.opengis.net/gml/3.2}Polygon")
            polygonElement.attrib["srsName"] = "http://www.opengis.net/gml/srs/epsg.xml#4326"
            
            polString = polString.replace("(((","") \
                                 .replace(")))","") \
                                 .replace("((", "") \
                                 .replace("))", "")
                                 
            #print polString
                                 
            polStringList = polString.split("),(")
            
            exteriorString = polStringList[0].replace(",", " ").strip()
            exteriorString = formatPositionFloats(exteriorString, 3)
            
            exteriorElement     = ET.SubElement(polygonElement   , "{http://www.opengis.net/gml/3.2}exterior")
            linearRingElement   = ET.SubElement(exteriorElement, "{http://www.opengis.net/gml/3.2}LinearRing")
            posListElement      = ET.SubElement(linearRingElement , "{http://www.opengis.net/gml/3.2}posList")
            posListElement.text = exteriorString
            
            # Delete Exterior posList from list => only interiors stay in the list
            del polStringList[0]
            
            for interiorString in polStringList:
                interiorString = interiorString.replace(",", " ")
                interiorString = formatPositionFloats(interiorString, 3)
                
                interiorElement = ET.SubElement(polygonElement, "{http://www.opengis.net/gml/3.2}interior")
                interiorLinearRingElement = ET.SubElement(interiorElement, "{http://www.opengis.net/gml/3.2}LinearRing")
                interiorPosListElement = ET.SubElement(interiorLinearRingElement, "{http://www.opengis.net/gml/3.2}posList")
                interiorPosListElement.text = interiorString
            polygonElementList.append(polygonElement)
        geomElementList = polygonElementList
    
    #print "len = " + str(geomElementList.__len__())
    return geomElementList 

#===============================================================================
def getExtent(featureClassList):
    
    extentList   = []
    maxXList = []
    minXList = []
    maxYList = []
    minYList = []
    
    
    for inFc in featureClassList:
        extent = arcpy.Describe(inFc).extent
        maxX = extent.XMin
        maxXList.append(maxX)
        minX = extent.XMax
        minXList.append(minX)
        maxY = extent.YMin
        maxYList.append(maxY)
        minY = extent.YMax
        minYList.append(minY)
    
    maxX = max(maxXList)
    extentList.append(maxX)
    minX = min(minXList)
    extentList.append(minX)
    maxY = max(maxYList)
    extentList.append(maxY)
    minY = min(minYList)
    extentList.append(minY)
    
    return extentList
        
 
