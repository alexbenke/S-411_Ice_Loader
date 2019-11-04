import arcpy
import os
import util
import s411objects

def iceareaToS411Objects(shpFile):
    s411SeaIceFeatureList = []
    
    shpFile = os.path.normpath(shpFile)
    
    # Multipart to Singlepart, because s411 does not support multigeometries
    # create temporary fgdb,because it is only possible
    # to perform Multipart to Singlepart with ESRI fgdb in arcpy
    
    #fgdbName = os.path.basename(shpFile)
    #print fgdbName
    #fgdbPath = os.path.dirname(shpFile)
    #print fgdbPath
    
    singleShpFile = shpFile
    
    #fgdb = util.createTemporaryFgdb(fgdbPath, fgdbName)
    #fgdb = os.path.normpath(fgdb).replace("\\", "/")
    #single means single geometries
    #singleShpFile = fgdb + "/" + "iceAreaSingle"
    #print singleShpFile
    #if arcpy.Exists(fgdb):
    #    arcpy.MultipartToSinglepart_management(fgdb, singleShpFile)
    #singleShpFile = "temp.shp"
    #arcpy.MultipartToSinglepart_management(shpFile, singleShpFile)
    
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
        ab = row.AB
        tmax = row.Tmax
        iceflz = row.ICEFLZ
        icercn = row.ICERCN
        icefcn = row.ICEFCN
        icefty = row.ICEFTY
        icemlt = row.ICEMLT
        geometry = row.getValue(geomFieldName).WKT
        
        #feature id for gml
        if fid is not None:
            s411SeaIceFeature.set_gml_id(fid)
            
        # ICEACT
                # ab -> xml element = iceact
        if ab is not None and ab != 0:
            if ab == 1:
                s411SeaIceFeature.set_iceact("1")
            elif ab == 2:
                s411SeaIceFeature.set_iceact("13")
            elif ab == 3:
                s411SeaIceFeature.set_iceact("46")
            elif ab == 4:
                s411SeaIceFeature.set_iceact("78")
            elif ab == 5:
                s411SeaIceFeature.set_iceact("91")
            elif ab == 6:
                s411SeaIceFeature.set_iceact("50")
            elif ab == 7:
                s411SeaIceFeature.set_iceact("92")
            elif ab == 8:
                s411SeaIceFeature.set_iceact("92")
            else:
                s411SeaIceFeature.set_iceact("99")
        else:
            s411SeaIceFeature.set_iceact("")
                
        # ICESOD
        # calculate icesod only from tmax not from tmin and tmax together because of safety 
        # issues       
        if tmax is not None:
            if tmax > 0  and tmax < 10:
                s411SeaIceFeature.set_icesod("81")
            elif tmax >= 10 and tmax < 15:
                s411SeaIceFeature.set_icesod("84")
            elif tmax >= 15 and tmax < 30:
                s411SeaIceFeature.set_icesod("85")
            elif tmax >= 30 and tmax < 50:
                s411SeaIceFeature.set_icesod("88")
            elif tmax >= 50 and tmax < 70:
                s411SeaIceFeature.set_icesod("89")
            elif tmax >= 70 and tmax < 120:
                s411SeaIceFeature.set_icesod("91")
            elif tmax >= 120 and tmax < 150:
                s411SeaIceFeature.set_icesod("93")
            elif tmax >= 150 and tmax < 250:
                s411SeaIceFeature.set_icesod("96")
            elif tmax >= 250:
                s411SeaIceFeature.set_icesod("97")
            else:
                s411SeaIceFeature.set_icesod("99")
        else:
            s411SeaIceFeature.set_icesod("")
             
        # ICEFTY
        if icefty is not None and icefty != 0:
            if icefty == 1:
                s411SeaIceFeature.set_icefty("1")
            elif icefty == 2:
                s411SeaIceFeature.set_icefty("2")
            elif icefty == 3:
                s411SeaIceFeature.set_icefty("3")
            elif icefty == 4:
                s411SeaIceFeature.set_icefty("4")
            elif icefty == 5:
                s411SeaIceFeature.set_icefty("5")
        else:
            s411SeaIceFeature.set_icefty("")
        # ICEFLZ
        if iceflz is not None and iceflz != 0:
            if iceflz == 1:
                s411SeaIceFeature.set_iceflz("2")
            elif iceflz == 2:
                s411SeaIceFeature.set_iceflz("3")
            elif iceflz == 3:
                s411SeaIceFeature.set_iceflz("4")
            elif iceflz == 4:
                s411SeaIceFeature.set_iceflz("5")
            elif iceflz == 5:
                s411SeaIceFeature.set_iceflz("6")
            elif iceflz == 6:
                s411SeaIceFeature.set_iceflz("7")
            elif iceflz == 7:
                s411SeaIceFeature.set_iceflz("8")
            elif iceflz == 8:
                s411SeaIceFeature.set_iceflz("9")
            elif iceflz == 9:
                s411SeaIceFeature.set_iceflz("10")
            else:
                s411SeaIceFeature.set_iceflz("99")
        else:
            s411SeaIceFeature.set_iceflz("")
                    
                    
            # ICERCN
        if icercn is not None and icercn != 0:
            if icercn == 1:
                s411SeaIceFeature.set_icercn("10")
            elif icercn == 3:
                s411SeaIceFeature.set_icercn("20")
            elif icercn == 5:
                s411SeaIceFeature.set_icercn("30")
            elif icercn == 7:
                s411SeaIceFeature.set_icercn("40")
            elif icercn == 9:
                s411SeaIceFeature.set_icercn("50")
            else:
                s411SeaIceFeature.set_icercn("99")
        else:
            s411SeaIceFeature.set_icercn("")
        
                    
        # ICEFCN
        if icefcn is not None and icefcn != 0:
            if icefcn == 1:
                s411SeaIceFeature.set_icefcn("10")
            elif icefcn == 3:
                s411SeaIceFeature.set_icefcn("20")
            elif icefcn == 5:
                s411SeaIceFeature.set_icefcn("30")
            elif icefcn == 7:
                s411SeaIceFeature.set_icefcn("40")
            elif icefcn == 9:
                s411SeaIceFeature.set_icefcn("50")
            else:
                s411SeaIceFeature.set_icefcn("99")
        else:
            s411SeaIceFeature.set_icefcn("")
                    
        # ICEMLT
        if icemlt is not None and icemlt != 0:
            if icemlt == 1:
                s411SeaIceFeature.set_icemlt("1")
            elif icemlt == 2:
                s411SeaIceFeature.set_icemlt("2")
            elif icemlt == 3:
                s411SeaIceFeature.set_icemlt("3")
            elif icemlt == 4:
                s411SeaIceFeature.set_icemlt("4")
            elif icemlt == 5:
                s411SeaIceFeature.set_icemlt("5")
            elif icemlt == 6:
                s411SeaIceFeature.set_icemlt("6")
            elif icemlt == 7:
                s411SeaIceFeature.set_icemlt("7")
            else:
                s411SeaIceFeature.set_icemlt("99")
        else:
            s411SeaIceFeature.set_icemlt("")
        
        
        
        # geometry as WKT to seaice feature
        
        if geometry is not None:
            s411SeaIceFeature.set_geometry(geometry)
            
        s411SeaIceFeatureList.append(s411SeaIceFeature)
        
    return s411SeaIceFeatureList

def icesymbolToS411Objects(shpFile):
    s411FeatureList = []
    
    shpFile = os.path.normpath(shpFile)
    singleShpFile = shpFile
    # Multipart to Singlepart, because s411 does not support multigeometries
    # create temporary fgdb,because it is only possible
    # to perform Multipart to Singlepart with ESRI fgdb in arcpy
    
    #fgdbName = os.path.basename(shpFile)
    #fgdbPath = os.path.dirname(shpFile)
    #
    #fgdb = util.createTemporaryFgdb(fgdbPath, fgdbName)
    
    # single means single geometries
    #singleShpFile = fgdb + "/" + "icesymbol"
    
    #arcpy.MultipartToSinglepart_management(fgdb, singleShpFile)
    
    # Get Name of Geometry Field for use during the reading of geometry attributes
    geomFieldName = arcpy.Describe(singleShpFile).shapeFieldName
    # Get feature id for using in gml-id
    fidFieldName = arcpy.Describe(singleShpFile).OIDFieldName
    
    rows = arcpy.SearchCursor(singleShpFile)
    
    for row in rows:
        
        # Create seaice object
        symbolNr = row.Symbol
        
        if symbolNr is not None:
            gmlId = row.getValue(fidFieldName)
            # Geometry as WKT
            geometry = row.getValue(geomFieldName).WKT
            
            feature = None
            
            if symbolNr == 1:
                feature = s411objects.Icerft()
            
            if symbolNr == 2:
                feature = s411objects.Flobrg()
                
            if symbolNr == 3:
                feature = s411objects.Icerdg()
                
            if symbolNr == 4:
                feature = s411objects.Jmdbrr()
                
            if symbolNr == 6:
                feature = s411objects.Icefra()
            
            feature.set_gml_id(gmlId)
            feature.set_geometry(geometry)
            s411FeatureList.append(feature)
            
    return s411FeatureList

def iceedgeToS411Objects(shpFile):
    
    s411IceEdgeList = []
    
    shpFile = os.path.normpath(shpFile)
    singleShpFile = shpFile
    # Multipart to Singlepart, because s411 does not support multigeometries
    # create temporary fgdb,because it is only possible
    # to perform Multipart to Singlepart with ESRI fgdb in arcpy
    
    #fgdbName = os.path.basename(shpFile)
    #fgdbPath = os.path.dirname(shpFile)
    
    #fgdb = util.createTemporaryFgdb(fgdbPath, fgdbName)
    
    # single means single geometries
    #singleShpFile = fgdb + "/" + "iceedge"
    
    #arcpy.MultipartToSinglepart_management(fgdb, singleShpFile)
    
    # Get Name of Geometry Field for use during the reading of geometry attributes
    geomFieldName = arcpy.Describe(singleShpFile).shapeFieldName
    # Get feature id for using in gml-id
    fidFieldName = arcpy.Describe(singleShpFile).OIDFieldName
    
    
    # Iterate trough icearea featues and put into S-411 Objects
    rows = arcpy.SearchCursor(singleShpFile)
    
    for row in rows:
        s411IceEdge = s411objects.Icelne()
        s411IceEdge.set_gml_id(row.getValue(fidFieldName))
        s411IceEdge.set_geometry(row.getValue(geomFieldName).WKT)
        s411IceEdgeList.append(s411IceEdge)
    
    return s411IceEdgeList

def bshiceToS411Objects(iceareaShp, icesymbolShp, iceedgeShp):
    s411Objects = []
    s411IceareaList = iceareaToS411Objects(iceareaShp)
    s411IceSymbList = icesymbolToS411Objects(icesymbolShp)
    s411IceEdgeList = iceedgeToS411Objects(iceedgeShp)
    
    if s411IceareaList.__len__() > 0:
        for icearea in s411IceareaList:
            s411Objects.append(icearea)
            
    if s411IceSymbList.__len__() > 0:
        for icesymb in s411IceSymbList:
            s411Objects.append(icesymb)
            
    if s411IceEdgeList.__len__() > 0:
        for iceedge in s411IceEdgeList:
            s411Objects.append(iceedge)
    
    return s411Objects