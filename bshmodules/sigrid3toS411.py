import s411
import arcpy

shp = arcpy.GetParameterAsText(0)

producer = arcpy.GetParameterAsText(1)

s411.sigrid3ToS411ExchangeSet(shp, producer)