'''
Created on 21.02.2014

@author: bm1281
'''
import arcpy
import os
import binascii

def createTemporaryFgdb(path, name):
    tmpFgdbPath = None
    if not os.path.exists(path + "/" + name + ".gdb"):
        arcpy.CreateFileGDB_management(path, name + ".gdb")
        tmpFgdbPath = path + "/" + name + ".gdb"
    else:
        tmpFgdbPath = path + "/" + name + ".gdb"
    
    return tmpFgdbPath

def getDirFromFilePath(filePath):
    openedFile = open(filePath)
    #fileDir = os.path.dirname(openedFile)
    basename = os.path.basename(filePath)
    fileDir = str(filePath).replace(str(basename), "")
    openedFile.close()
    
    return fileDir
    
def deleteTemporaryFgdb(fgdbPath):
    
    if os.path.exists(fgdbPath):
        arcpy.Delete_management(fgdbPath)
        
def cleanWorkspace(path, name):
    deleteTemporaryFgdb(path + name + ".gdb")
    
def calculateCRCCode(path):
    buf = open(path,'rb').read()
    #buf = (binascii.crc_hqx(buf,0) & 0xFFFFFFFF)
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    #print type(buf)
    return buf
    #return "%08X" % buf
