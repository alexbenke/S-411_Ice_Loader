from xml.etree import ElementTree as ET
import geometry
import os
import glob
from bshice import bshiceToS411Objects
import s411metadata
import s411objects
import bshice
import arcpy
import datetime, time

import zipfile
import zlib
def zipdir(path, zip):
	# writes a full directory to a zipfile
	# filenames within the zipfile begin with the directoryname
	# without the full path before the directory
	compression = zipfile.ZIP_DEFLATED
	for root, dirs, files in os.walk(path):
		for file in files:
			ARCNAME=os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
			zip.write(os.path.join(root, file),arcname=ARCNAME, compress_type=compression)
			

def s411ObjectsToGml(s411ObjectList):
    
    ############ ENUMS #############
    iceactEnum = [1,2,3,10,12,13,20,23,24,30,34,35,40,45,46,70,78,79,80,89,90,91,92,99]
    iceapcEnum = [1,2,3,10,12,13,20,23,24,30,34,35,40,45,46,70,78,79,80,89,90,91,92,99]
    icesodEnum = [1,70,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
    icelsoEnum = [1,2,3,4,5,70,99]
    iceflzEnum = [1,2,3,4,5,6,7,8,9,10,11,99]
    icemltEnum = [1,2,3,4,5,6,7,8,9,10,99]
    icespcEnum = [11,12,13,14,15,16,17,18,19,20,99]
    #icebnm
    icelvlEnum = [1,2,99]
    icecstEnum = [1,10,12,20,23,30,98,99]
    iceftyEnum = [1,2,3,4,5]
    icelstEnum = [1,2,99]
    #icelfq
    icelorEnum = [1,2,3,4,5,6,7,8,9,10,99]
    #icelwd
    icelocEnum = [1,2]
    icebszEnum = [1,2,3,4,5,6,7,8,9,99]
    iceddrEnum = [1,2,3,4,5,6,7,8,9,10,99]
    #icedsp
    #icetck
    #icemax
    #icemin
    icettyEnum = [1,2,99]
    #icesct
    icescnEnum = [1,2,3,4,5,6,7,8,9,10,11,12,99]
    icedosEnum = [1,2,3,4,5,6,7,8,9,10,99]
    icercnEnum = [1,10,12,20,23,30,34,40,45,50,56,60,67,70,78,80,89,90,91,92,98,99]
    icerdvEnum = [1,2,3,4,5,6,7,8,99]
    #icermh
    #icerfq
    #icerxh
    icekcnEnum = [1,10,12,20,23,30,34,40,45,50,56,60,67,70,78,80,89,90,91,92,98,99]
    #icekfq
    #icekmd
    #icekxd
    icefcnEnum = [1,10,12,20,23,30,34,40,45,50,56,60,67,70,78,80,89,90,91,92,98,99]
    #ia_sfa & co. 
    ia_sngEnum = [1,10,12,20,23,30,98,99]
    ia_mltEnum = [1,10,12,20,23,30,34,40,45,50,98,99]
    ia_plgEnum = [1,10,12,20,23,30,98,99]
    ia_hlgEnum = [1,10,12,20,23,30,98,99]
    ia_dugEnum = [10,20,30,40,50,60,70,80,90,92,98,99]
    ia_bcnEnum = [10,12,20,23,30,34,40,45,50,56,60,67,70,78,80,89,90,98,99]
    ia_bfmEnum = [1,2,3,4,5,6,7,8,99]
    #ia_buh
    #ia_obn
    #ia_dxw
    #ia_dmw
    #icebrsEnum = [1,10,12,20,23,30,34,40,45,50,56,60,67,70,78,80,89,90,91,92,98,99]
    
    ################################
    
    s411ElementList = []
    
    ET.register_namespace("ice", "http://www.jcomm.info/ice")
    ET.register_namespace("gml" , "http://www.opengis.net/gml/3.2")
    
    for s411Object in s411ObjectList:
        typeName = type(s411Object).__name__
        
        iceFeatureMemberElement = ET.Element("{http://www.jcomm.info/ice}IceFeatureMember")
        
        iceElement = None # for storing of ice feature elements
        
        # seaice
        if typeName == "Seaice":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}seaice")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "seaice." + str(str(s411Object.get_gml_id()))
            
            try:
                if s411Object.get_iceact() is not None and s411Object.get_iceact() != "":# and s411Object.get_iceact() in iceactEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceact")
                    if(str(s411Object.get_iceact()).strip() is not None):
                        element.text = str(s411Object.get_iceact())
            except AttributeError:
                pass
                 
            try:
                if s411Object.get_iceapc() is not None and s411Object.get_iceapc() != 0:# and s411Object.get_iceapc() in iceapcEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceapc")
                    element.text = str(s411Object.get_iceapc())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icesod() is not None and s411Object.get_icesod() != "":#and s411Object.get_icesod() in icesodEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesod")
                    element.text = str(s411Object.get_icesod())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_iceflz() is not None and s411Object.get_iceflz() != "":#and s411Object.get_iceflz() in iceflzEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceflz")
                    element.text = str(s411Object.get_iceflz())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icespc() is not None and s411Object.get_icespc() != "":#and s411Object.get_icespc() in icespcEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icespc")
                    element.text = str(s411Object.get_icespc())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icelvl() is not None and s411Object.get_icelvl() != "":#and s411Object.get_icelvl() in icelvlEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelvl")
                    element.text = str(s411Object.get_icelvl())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icecst() is not None and s411Object.get_icecst() != "":#and s411Object.get_icecst() in icecstEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icecst")
                    element.text = str(s411Object.get_icecst())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icefty() is not None :#and s411Object.get_icefty() in iceftyEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icefty")
                    element.text = str(s411Object.get_icefty())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icedsp() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedsp")
                    element.text = str(s411Object.get_icedsp())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_iceddr() is not None :#and s411Object.get_iceddr() in iceddrEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceddr")
                    element.text = str(s411Object.get_iceddr())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icercn() is not None :#and s411Object.get_icercn() in icercnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icercn")
                    element.text = str(s411Object.get_icercn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icerfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerfq")
                    element.text = str(s411Object.get_icerfq())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icermh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icermh")
                    element.text = str(s411Object.get_icermh())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icerxh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerxh")
                    element.text = str(s411Object.get_icerxh())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icerdv() is not None :#and s411Object.get_icerdv() in icerdvEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerdv")
                    element.text = str(s411Object.get_icerdv())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekcn() is not None :#and s411Object.get_icekcn() in icekcnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekcn")
                    element.text = str(s411Object.get_icekcn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekfq")
                    element.text = str(s411Object.get_icekfq())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekmd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekmd")
                    element.text = str(s411Object.get_icekmd())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icekxd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekxd")
                    element.text = str(s411Object.get_icekxd())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icefcn() is not None :#and s411Object.get_icefcn() in icefcnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icefcn")
                    element.text = str(s411Object.get_icefcn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icetck() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icetck")
                    element.text = str(s411Object.get_icetck())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icemax() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemax")
                    element.text = str(s411Object.get_icemax())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icemin() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemin")
                    element.text = str(s411Object.get_icemin())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icetty() is not None :#and s411Object.get_icetty() in icettyEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icetty")
                    element.text = str(s411Object.get_icetty())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icemlt() is not None :#and s411Object.get_icemlt() in icemltEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemlt")
                    element.text = str(s411Object.get_icemlt())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icescn() is not None :#and s411Object.get_icescn() in icescnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icescn")
                    element.text = str(s411Object.get_icescn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icesct() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesct")
                    element.text = str(s411Object.get_icesct())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icedos() is not None :#and s411Object.get_icedos() in icedosEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedos")
                    element.text = str(s411Object.get_icedos())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icelst() is not None :#and s411Object.get_icelst() in icelstEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelst")
                    element.text = str(s411Object.get_icelst())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icelfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelfq")
                    element.text = str(s411Object.get_icelfq())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icelor() is not None :#and s411Object.get_icelor() in icelorEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelor")
                    element.text = str(s411Object.get_icelor())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icelwd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelwd")
                    element.text = str(s411Object.get_icelwd())
            except AttributeError:
                pass
            
#             ia_sfa = s411Object.get_ia_sfa()
#             ia_sfb = s411Object.get_ia_sfb()
#             ia_sfc = s411Object.get_ia_sfc()
#             ia_ffa = s411Object.get_ia_ffa()
#             ia_ffb = s411Object.get_ia_ffb()
#             ia_ffc = s411Object.get_ia_ffc()
            
            try:
                if s411Object.get_ia_sng() is not None :#and s411Object.get_ia_sng() in ia_sngEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_sng")
                    element.text = str(s411Object.get_ia_sng())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_mlt() is not None :#and s411Object.get_ia_mlt() in ia_mltEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_mlt")
                    element.text = str(s411Object.get_ia_mlt())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_plg() is not None :#and s411Object.get_ia_plg() in ia_plgEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_plg")
                    element.text = str(s411Object.get_ia_plg())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_hlg() is not None :#and s411Object.get_ia_hlg() in ia_hlgEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_hlg")
                    element.text = str(s411Object.get_ia_hlg())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_dug() is not None :#and s411Object.get_ia_dug() in ia_dugEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dug")
                    element.text = str(s411Object.get_ia_dug())
            except AttributeError:
                pass
                
        # lacice
        if typeName == "Lacice":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}lacice")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "lacice." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_iceact() is not None :#and s411Object.get_iceact() in iceactEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceact")
                    element.text = str(s411Object.get_iceact())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_iceapc() is not None :#and s411Object.get_iceapc() in iceapcEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceapc")
                    element.text = str(s411Object.get_iceapc())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icelso() is not None :#and s411Object.get_icelso() in icesodEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesod")
                    element.text = str(s411Object.get_icelso())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_iceflz() is not None :#and s411Object.get_iceflz() in iceflzEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceflz")
                    element.text = str(s411Object.get_iceflz())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icespc() is not None :#and s411Object.get_icespc() in icespcEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icespc")
                    element.text = str(s411Object.get_icespc())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icelvl() is not None :#and s411Object.get_icelvl() in icelvlEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelvl")
                    element.text = str(s411Object.get_icelvl())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icecst() is not None :#and s411Object.get_icecst() in icecstEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icecst")
                    element.text = str(s411Object.get_icecst())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icefty() is not None :#and s411Object.get_icefty() in iceftyEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icefty")
                    element.text = str(s411Object.get_icefty())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icedsp() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedsp")
                    element.text = str(s411Object.get_icedsp())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_iceddr() is not None :#and s411Object.get_iceddr() in iceddrEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceddr")
                    element.text = str(s411Object.get_iceddr())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icercn() is not None :#and s411Object.get_icercn() in icercnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icercn")
                    element.text = str(s411Object.get_icercn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icerfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerfq")
                    element.text = str(s411Object.get_icerfq())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icermh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icermh")
                    element.text = str(s411Object.get_icermh())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icerxh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerxh")
                    element.text = str(s411Object.get_icerxh())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icerdv() is not None :#and s411Object.get_icerdv() in icerdvEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerdv")
                    element.text = str(s411Object.get_icerdv())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekcn() is not None :#and s411Object.get_icekcn() in icekcnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekcn")
                    element.text = str(s411Object.get_icekcn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekfq")
                    element.text = str(s411Object.get_icekfq())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekmd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekmd")
                    element.text = str(s411Object.get_icekmd())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icekxd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekxd")
                    element.text = str(s411Object.get_icekxd())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icefcn() is not None :#and s411Object.get_icefcn() in icefcnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icefcn")
                    element.text = str(s411Object.get_icefcn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icetck() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icetck")
                    element.text = str(s411Object.get_icetck())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icemax() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemax")
                    element.text = str(s411Object.get_icemax())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icemin() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemin")
                    element.text = str(s411Object.get_icemin())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icetty() is not None :#and s411Object.get_icetty() in icettyEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icetty")
                    element.text = str(s411Object.get_icetty())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icemlt() is not None :#and s411Object.get_icemlt() in icemltEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemlt")
                    element.text = str(s411Object.get_icemlt())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icescn() is not None :#and s411Object.get_icescn() in icescnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icescn")
                    element.text = str(s411Object.get_icescn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icesct() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesct")
                    element.text = str(s411Object.get_icesct())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icedos() is not None :#and s411Object.get_icedos() in icedosEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedos")
                    element.text = str(s411Object.get_icedos())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icelst() is not None :#and s411Object.get_icelst() in icelstEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelst")
                    element.text = str(s411Object.get_icelst())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icelfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelfq")
                    element.text = str(s411Object.get_icelfq())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icelor() is not None :#and s411Object.get_icelor() in icelorEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelor")
                    element.text = str(s411Object.get_icelor())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icelwd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelwd")
                    element.text = str(s411Object.get_icelwd())
            except AttributeError:
                pass
        
        
        # brgare
        if typeName == "Brgare":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}brgare")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "brgare." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icebnm() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icebnm")
                    element.text = str(s411Object.get_icebnm())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icebsz() is not None :#and s411Object.get_icebsz() in icebszEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icebsz")
                    element.text = str(s411Object.get_icebsz())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_bcn() is not None :#and s411Object.get_ia_bcn() in ia_bcnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_bcn")
                    element.text = str(s411Object.get_ia_bcn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_bfm() is not None :#and s411Object.get_ia_bfm() in ia_bfmEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_bfm")
                    element.text = str(s411Object.get_ia_bfm())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_buh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_buh")
                    element.text = str(s411Object.get_ia_buh())
            except AttributeError:
                pass
            
        # icelne
        if typeName == "Icelne":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icelne")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icelne." + str(s411Object.get_gml_id())
            
        # brglne
        if typeName == "Brglne":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}brglne")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "brglne." + str(s411Object.get_gml_id())
            
        # opnlne
        if typeName == "Opnlne":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}opnlne")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "opnlne." + str(s411Object.get_gml_id())
            
        # lkilne
        if typeName == "Lkilne":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}lkilne")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "lkilne." + str(s411Object.get_gml_id())
            
        #i ridg
        if typeName == "I_Ridg":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}i_ridg")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "i_ridg." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icerdv() is not None :#and s411Object.get_icerdv() in icerdvEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerdv")
                    element.text = str(s411Object.get_icerdv())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icermh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icermh")
                    element.text = str(s411Object.get_icermh())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icerxh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerxh")
                    element.text = str(s411Object.get_icerxh())
            except AttributeError:
                pass
                
        #i lead
        if typeName == "I_Lead":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}i_lead")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "i_lead." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icesod() is not None :#and s411Object.get_icesod() in icesodEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesod")
                    element.text = str(s411Object.get_icesod())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_obn() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_obn")
                    element.text = str(s411Object.get_ia_obn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icedvw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedvw")
                    element.text = str(s411Object.get_icedvw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dmw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dmw")
                    element.text = str(s411Object.get_ia_dmw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dxw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dxw")
                    element.text = str(s411Object.get_ia_dxw())
            except AttributeError:
                pass
                
        #i fral
        if typeName == "I_Fral":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}i_fral")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "i_fral." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icesod() is not None :#and s411Object.get_icesod() in icesodEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesod")
                    element.text = str(s411Object.get_icesod())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_obn() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_obn")
                    element.text = str(s411Object.get_ia_obn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icedvw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedvw")
                    element.text = str(s411Object.get_icedvw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dmw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dmw")
                    element.text = str(s411Object.get_ia_dmw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dxw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dxw")
                    element.text = str(s411Object.get_ia_dxw())
            except AttributeError:
                pass
                
        #i crac
        if typeName == "I_Crac":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}i_crac")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "i_crac." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icesod() is not None :#and s411Object.get_icesod() in icesodEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesod")
                    element.text = str(s411Object.get_icesod())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_obn() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_obn")
                    element.text = str(s411Object.get_ia_obn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icedvw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedvw")
                    element.text = str(s411Object.get_icedvw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dmw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dmw")
                    element.text = str(s411Object.get_ia_dmw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dxw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dxw")
                    element.text = str(s411Object.get_ia_dxw())
            except AttributeError:
                pass
                
        # Icecom     
        if typeName == "Icecom":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icecom")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icecom." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icecst() is not None :#and s411Object.get_icecst() in icecstEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icecst")
                    element.text = str(s411Object.get_icecst())
            except AttributeError:
                pass
        
        # Icelea
        if typeName == "Icelea":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icelea")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icelea." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_iceloc() is not None :#and s411Object.get_iceloc() in icelocEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceloc")
                    element.text = str(s411Object.get_iceloc())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icelst() is not None :#and s411Object.get_icelst() in icelstEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelst")
                    element.text = str(s411Object.get_icelst())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icelwd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icelwd")
                    element.text = str(s411Object.get_icelwd())
            except AttributeError:
                pass
            
        # Icebrg
        if typeName == "Icebrg":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icebrg")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icebrg." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icebsz() is not None :#and s411Object.get_icebsz() in icebszEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icebsz")
                    element.text = str(s411Object.get_icebsz())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icedsp() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedsp")
                    element.text = str(s411Object.get_icedsp())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_iceddr() is not None :#and s411Object.get_iceddr() in iceddrEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceddr")
                    element.text = str(s411Object.get_iceddr())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_obn() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_obn")
                    element.text = str(s411Object.get_ia_obn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_bfm() is not None :#and s411Object.get_ia_bfm() in ia_bfmEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_bfm")
                    element.text = str(s411Object.get_ia_bfm())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_ia_buh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_buh")
                    element.text = str(s411Object.get_ia_buh())
            except AttributeError:
                pass
                
        # Flobrg
        if typeName == "Flobrg":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}flobrg")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "flobrg." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icedsp() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedsp")
                    element.text = str(s411Object.get_icedsp())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_iceddr() is not None :#and s411Object.get_iceddr() in iceddrEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceddr")
                    element.text = str(s411Object.get_iceddr())
            except AttributeError:
                pass
                
        # icethk
        if typeName == "Icethk":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icethk")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icethk." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icetck() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icetck")
                    element.text = str(s411Object.get_icetck())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icemax() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemax")
                    element.text = str(s411Object.get_icemax())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icemin() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemin")
                    element.text = str(s411Object.get_icemin())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icetty() is not None :#and s411Object.get_icetty() in icettyEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icetty")
                    element.text = str(s411Object.get_icetty())
            except AttributeError:
                pass
                
        
        # iceshr
        if typeName == "Iceshr":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}iceshr")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "iceshr." + str(s411Object.get_gml_id())
            
        # icediv
        if typeName == "Icediv":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icediv")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icediv." + str(s411Object.get_gml_id())
            
        # icerdg
        if typeName == "Icerdg":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icerdg")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icerdg." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icercn() is not None :#and s411Object.get_icercn() in icercnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icercn")
                    element.text = str(s411Object.get_icercn())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icerfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerfq")
                    element.text = str(s411Object.get_icerfq())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icermh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icermh")
                    element.text = str(s411Object.get_icermh())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icerxh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerxh")
                    element.text = str(s411Object.get_icerxh())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icerdv() is not None :#and s411Object.get_icerdv() in icerdvEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icerdv")
                    element.text = str(s411Object.get_icerdv())
            except AttributeError:
                pass
                
        # icekel
        if typeName == "Icekel":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icekel")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icekel." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icekcn() is not None :#and s411Object.get_icekcn() in icekcnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekcn")
                    element.text = str(s411Object.get_icekcn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icekfq() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekfq")
                    element.text = str(s411Object.get_icekfq())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekmd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekmd")
                    element.text = str(s411Object.get_icekmd())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_icekxd() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icekxd")
                    element.text = str(s411Object.get_icekxd())
            except AttributeError:
                pass
                
        # icedft
        if typeName == "Icedft":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icedft")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icedft." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icedsp() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedsp")
                    element.text = str(s411Object.get_icedsp())
            except AttributeError:
                pass
                
            try:
                if s411Object.get_iceddr() is not None :#and s411Object.get_iceddr() in iceddrEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceddr")
                    element.text = str(s411Object.get_iceddr())
            except AttributeError:
                pass
                
        # icefra
        if typeName == "Icefra":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icefra")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icefra." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icefty() is not None :#and s411Object.get_icefty() in iceftyEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icefty")
                    element.text = str(s411Object.get_icefty())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_iceloc() is not None :#and s411Object.get_iceloc() in icelocEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}iceloc")
                    element.text = str(s411Object.get_iceloc())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_obn() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_obn")
                    element.text = str(s411Object.get_ia_obn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icesod() is not None :#and s411Object.get_icesod() in icesodEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesod")
                    element.text = str(s411Object.get_icesod())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icedvw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedvw")
                    element.text = str(s411Object.get_icedvw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dmw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dmw")
                    element.text = str(s411Object.get_ia_dmw())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_ia_dxw() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_dxw")
                    element.text = str(s411Object.get_ia_dxw())
            except AttributeError:
                pass
                
        # icerft
        if typeName == "Icerft":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}icerft")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "icerft." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icefcn() is not None :#and s411Object.get_icefcn() in icefcnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icefcn")
                    element.text = str(s411Object.get_icefcn())
            except AttributeError:
                pass
                
        # jmdbrr
        if typeName == "Jmdbrr":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}jmdbrr")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "jmdbrr." + str(s411Object.get_gml_id())
            
        # stgmlt
        if typeName == "Stgmlt":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}stgmlt")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "stgmlt." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icemlt() is not None :#and s411Object.get_icemlt() in icemltEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icemlt")
                    element.text = str(s411Object.get_icemlt())
            except AttributeError:
                pass
                
        # snwcvr
        if typeName == "Snwcvr":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}snwcvr")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "snwcvr." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icescn() is not None :#and s411Object.get_icescn() in icescnEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icescn")
                    element.text = str(s411Object.get_icescn())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icesct() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icesct")
                    element.text = str(s411Object.get_icesct())
            except AttributeError:
                pass
            
            try:
                if s411Object.get_icedos() is not None :#and s411Object.get_icedos() in icedosEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icedos")
                    element.text = str(s411Object.get_icedos())
            except AttributeError:
                pass
                
        # strptc
        if typeName == "Strptc":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}strptc")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "strptc." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_icespc() is not None :#and s411Object.get_icespc() in icespcEnum:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}icespc")
                    element.text = str(s411Object.get_icespc())
            except AttributeError:
                pass
                
        # i_grhm
        if typeName == "I_Grhm":
            iceElement = ET.SubElement(iceFeatureMemberElement, "{http://www.jcomm.info/ice}i_grhm")
            iceElement.attrib["{http://www.opengis.net/gml/3.2}id"] = "i_grhm." + str(s411Object.get_gml_id())
            
            try:
                if s411Object.get_ia_buh() is not None:
                    element = ET.SubElement(iceElement, "{http://www.jcomm.info/ice}ia_buh")
                    element.text = str(s411Object.get_ia_buh())
            except AttributeError:
                pass
    
                    
        # geometry
        geomList = geometry.convertWktToGml(s411Object.get_geometry())
        
        # the geometry method above is useful also for multiple geoms, but after MultipartToSinglePart
        # the geometry of feature is the first element of geomList
        geomElement = geomList[0]
        geomElement.attrib["{http://www.opengis.net/gml/3.2}id"] = str(typeName).lower() + "." + str(s411Object.get_gml_id()) + "g"
        iceElement.append(geomElement)
        
       
        s411ElementList.append(iceFeatureMemberElement)
    # chekc if empty
#     for el in s411ElementList:
#         elList = list(el.iter())
#         for elem in elList:
#             elemValue = str(elem.text)
#             if elemValue is not None and elemValue == "":
#                 print "i am empty"
        
    return s411ElementList

def createS411DataSet(s411ElementList):
    ET.register_namespace("ice", "http://www.jcomm.info/ice")
    ET.register_namespace("gml" , "http://www.opengis.net/gml/3.2")
    
    # Create dataset element
    datasetElement = ET.Element("{http://www.jcomm.info/ice}IceDataSet")
    # append elements from elementsList
    for element in s411ElementList:
        datasetElement.append(element)
    # return tree (for using in crateExchangeSet)
    tree = ET.ElementTree(datasetElement)
    #tree.write("test.xml")
    return tree


# Hauptmetode	
def createS411ExchangeSet(s411path, s411name, datasetTree, metadataTree):
	# s411path - ordner wo Exchange Set erzeugt wird
	# s411name - name von Exchange Set  z.B. "S411_BSH_Ek_20140221"
	# datasetTree - createS411DataSet(s411ElementList), S411 List aus shp file, mit bshice.py bshiceToS411Objects()
	# metadataTree - import aus s411Metadata.py, getS411MetadataFromTemplate()

    s411ExchangeSetPath = s411path + os.path.sep + s411name
    if not os.path.exists(s411ExchangeSetPath):
        os.makedirs(s411ExchangeSetPath)
    dataPath = s411ExchangeSetPath + os.path.sep + "data"
    if not os.path.exists(dataPath):
        os.makedirs(dataPath)
    supportPath = s411ExchangeSetPath + os.path.sep + "support"
    if not os.path.exists(supportPath):
        os.makedirs(supportPath)
    datasetTree.write(dataPath + os.path.sep + s411name + ".gml", encoding='utf-8', xml_declaration=True)
    metadataTree.write(supportPath + os.path.sep  + s411name + ".gml.xml", encoding='utf-8', xml_declaration=True)
    
    
def createS411ExchangeSetsFromBshData(dirPath):
	dirList = os.listdir(dirPath)
	# perhaps easier using glob.glob("[eE][kK]*")
	for directory in dirList:
		ekPath = dirPath + os.path.sep + str(directory)
		if os.path.isdir(ekPath) and (str(directory).startswith("Ek") or str(directory).startswith("EK") or str(directory).startswith("ek")):
			ekPathFiles = os.listdir(ekPath)
			# perhaps easier using glob.glob("IceArea*.shp"), etc.
			# then also check that not multiple files are present
			if glob.glob(ekPath + os.path.sep + "S411_BSH*"): continue
			# this skips over the rest to continue with the next directory,
			# as the s411 output is already there
			fileList = []
			dateStamp = None
			for ekFile in ekPathFiles:
				if ekFile.startswith("IceArea") and ekFile.endswith(".shp"):
					iceareaPath = ekPath + os.path.sep + ekFile
					fileList.append(iceareaPath)
					# die dateStamp sollte besser aus den IceArea-Namen bestimmt werden!!!!
					# Temporal extent sollte auch besser gesetzt werden
					# bei uns wohl gültig für eine Woche bei Ek1, 1 oder 2 Tage bei Ek3
					# bei ek3 dann aber in den Metadaten reinschreiben, dass der Norden anders ist!
					dateStamp = os.path.getmtime(iceareaPath)
					dateStamp = str(datetime.datetime.fromtimestamp(dateStamp))
					dateStamp = dateStamp[:10].replace("-","")
				if ekFile.startswith("IceSymbol") and ekFile.endswith(".shp"):
					icesymbolPath = ekPath + os.path.sep + ekFile
					fileList.append(icesymbolPath)
				if ekFile.startswith("Estimated_Ice_Edge") and ekFile.endswith(".shp"):
					iceedgePath = ekPath + os.path.sep + ekFile
					fileList.append(iceedgePath)
                
			# print fileList.__len__()  
			extent = None
			if fileList.__len__() > 0:
				extent = geometry.getExtent(fileList)  
				# wenn das die geographic bounding bos setzen soll, funktionierts es nicht ganz richtig
			else:
				extent = [0,0,0,0]
            
			s411FeatureList = bshice.bshiceToS411Objects(iceareaPath, icesymbolPath, iceedgePath)
			s411FeatureElementsList = s411ObjectsToGml(s411FeatureList)
			datasetTree = createS411DataSet(s411FeatureElementsList)
			metadataTree = s411metadata.getS411MetadataFromTemplate("mdTemplateBshBaltic.xml", "S411_BSH_" + str(directory), dateStamp, extent, dateStamp, dateStamp)
			print "DIR=" + directory

			# the S411 directory structure is written to the subdirectory with the icearea
			createS411ExchangeSet(ekPath, "S411_BSH_" + directory, datasetTree, metadataTree)
			exchangeCatalogueTree = s411metadata.getS411ExchangeCatalogueFromTemplate("ecTemplateBsh.xml", metadataTree, "S411_BSH_" + str(directory), "S411_BSH_" + str(directory) + ".gml", extent, ekPath + os.path.sep + "S411_BSH_" + directory +  os.path.sep + "data" + os.path.sep +  "S411_BSH_" + directory + ".gml")
			exchangeCatalogueTree.write(ekPath + os.path.sep + "S411_BSH_" + str(directory) + os.path.sep + "catalogue.xml", encoding ='utf-8', xml_declaration=True)
			
			# a S411-zipfile is written to the chartdirectory =dirPath
			dumy=os.path.join(ekPath, "S411_BSH_" + directory)
			filename = os.path.join(dirPath, "S411_BSH_" + directory +'.zip')
			zf = zipfile.ZipFile(filename, mode='w')
			zipdir(dumy,zf)
			zf.close()

#iceedgePath = os.path.normpath("C:\Meereskunde\Vorhersagedienste\Eisdienst\Eisprodukte\Eisuebersichtskarte\Ek-20140130\Estimated_Ice_Edge140130.shp")
#iceareaPath = os.path.normpath("C:\Meereskunde\Vorhersagedienste\Eisdienst\Eisprodukte\Eisuebersichtskarte\Ek-20140130\IceArea.shp")
#lastmodTime = os.path.getmtime(iceareaPath)
#print lastmodTime
#icesymbPath = os.path.normpath("C:\Meereskunde\Vorhersagedienste\Eisdienst\Eisprodukte\Eisuebersichtskarte\Ek-20140130\IceSymbol.shp")
#fileList = [iceedgePath, iceareaPath, icesymbPath]
#s411path = os.path.dirname(iceareaPath)
#s411pathDirName = "S411_BSH_ " + os.path.basename(s411path)
#print s411pathDirName


#extent = geometry.getExtent(fileList)
#print extent[0]

#s411featureList = bshice.bshiceToS411Objects(iceareaPath, icesymbPath, iceedgePath)
#s411featureElementsList = s411ObjectsToGml(s411featureList)
#tree = createS411DataSet(s411featureElementsList)
#mtree = s411metadata.getS411MetadataFromTemplate("mdTemplateBshBaltic.xml", s411pathDirName, lastmodTime, extent, lastmodTime, lastmodTime)
#createS411ExchangeSet(s411path, s411pathDirName, tree, mtree)

chartDir = os.path.normpath("X:\Meereskunde\Vorhersagedienste\Eisdienst\Eisprodukte\Eisuebersichtskarte")
createS411ExchangeSetsFromBshData(chartDir)