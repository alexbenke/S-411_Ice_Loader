import arcpy
import os
import util
import s411objects

def sigrid3ToS411Objects(shpFile):
    
    s411SeaIceFeatureList = []
    
    shpFile = os.path.normpath(shpFile)
    

    # Multipart to Singlepart, because s411 does not support multigeometries
    # create temporary fgdb,because it is only possible
    # to perform Multipart to Singlepart with ESRI fgdb in arcpy
        
    #fgdbName = "a" + str(os.path.basename(shpFile)).replace(".shp", "").replace("-","_").replace(" ", "_")
    fgdbName = "tmp"
    print os.path.basename(shpFile)
    fgdbPath = os.path.dirname(shpFile)
    print fgdbPath
        
    fgdb = util.createTemporaryFgdb(fgdbPath, fgdbName)
    singleShpFile = fgdb + os.path.sep + "a" + fgdbName
        
    try:
        arcpy.MultipartToSinglepart_management(shpFile, singleShpFile)
    except arcpy.ExecuteError:
        arcpy.Delete_management(singleShpFile, None)
        try:
            arcpy.MultipartToSinglepart_management(shpFile, singleShpFile)
        except arcpy.ExecuteError:
            print arcpy.GetMessages()
        except Exception as e:
            print e
        
        
    # Get Name of Geometry Field for use during the reading of geometry attributes
    geomFieldName = arcpy.Describe(singleShpFile).shapeFieldName
    # Get feature id for using in gml-id
    fidFieldName = arcpy.Describe(singleShpFile).OIDFieldName
        
        
    # Iterate trough icearea featues and put into S-411 Objects
    rows = arcpy.SearchCursor(singleShpFile)
        
    for row in rows:
            
        # Create seaice object
        s411SeaIceFeature = s411objects.Seaice()
            
        fid = row.getValue(fidFieldName)
        ct = row.CT
        #ca = row.CA
        #cb = row.CB
        #cc = row.CC
        sa = row.SA
        #sb = row.SB
        #sc = row.SC
        fa = row.FA
        #fb = row.FB
        #fc = row.FC
        geometry = row.getValue(geomFieldName).WKT
            
        #feature id for gml
        if fid is not None:
            s411SeaIceFeature.set_gml_id(fid)
            
        # ICEACT from CT
        if ct is not None:
            if ct == 0:
                s411SeaIceFeature.set_iceact("1")
            elif ct == 1:
                s411SeaIceFeature.set_iceact("2")
            elif ct == 2:
                s411SeaIceFeature.set_iceact("3")
            elif str(ct) == "-9":
                pass
            else:
                s411SeaIceFeature.set_iceact(str(ct))
            
        # ICESOD from SA
        if sa is not None:
            if sa == 0:
                s411SeaIceFeature.set_icesod("1")
            elif str(sa) == "-9":
                pass
            else:
                s411SeaIceFeature.set_icesod(str(sa))
                
        # ICEFLZ fro FA
        if fa is not None:
            if fa == 0:
                s411SeaIceFeature.set_iceflz("1")
            elif fa == 1:
                s411SeaIceFeature.set_iceflz("2")
            elif fa == 2:
                s411SeaIceFeature.set_iceflz("3")
            elif str(fa) == "-9":
                pass
            else:
                s411SeaIceFeature.set_iceflz(str(fa))
                    
        # geometry as WKT to seaice feature
        
        if geometry is not None:
            s411SeaIceFeature.set_geometry(geometry)
                
        s411SeaIceFeatureList.append(s411SeaIceFeature)
        
    return s411SeaIceFeatureList
                    
                    