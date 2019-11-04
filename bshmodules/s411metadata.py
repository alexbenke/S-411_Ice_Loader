'''
Created on 24.02.2014

@author: bm1281
'''

from xml.etree import ElementTree as ET
import os
import util

def getS411MetadataFromTemplate(templateFilePath, dataSetId, dateStamp, extent, startDate, endDate):
                
        
        
    tree = ET.parse(templateFilePath)
        
    ET.register_namespace("gmd", "http://www.isotc211.org/2005/gmd")
    ET.register_namespace("gco", "http://www.isotc211.org/2005/gco")
    ET.register_namespace("gml", "http://www.opengis.net/gml/3.2")
        
    namespaces = {'gmd': 'http://www.isotc211.org/2005/gmd', "gco": "http://www.isotc211.org/2005/gco", "gml": "http://www.opengis.net/gml/3.2"}
        
    # file Identifier
    fileIdElement = tree.find("./gmd:fileIdentifier/gco:CharacterString", namespaces)
    fileIdElement.text = str(dataSetId)
        
    # date stamp
    dateStampElement = tree.find("./gmd:dateStamp/gco:Date", namespaces)
    dateStampElement.text = str(dateStamp)
        
    # identification Info
    titleElement = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString", namespaces)
    titleElement.text = str(dataSetId)
        
    idDateElement = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date", namespaces)
    idDateElement.text = str(dateStamp)
        
    westLonElement = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal", namespaces)
    westLonElement.text = str(extent[0])
        
    eastLonElement = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal", namespaces)
    eastLonElement.text = str(extent[1])
        
    southLatElement = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal", namespaces)
    southLatElement.text = str(extent[2])
        
    northLatElement = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal", namespaces)
    northLatElement.text = str(extent[3])
        
    #temporal extent
    beginDate = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:beginPosition", namespaces)
    beginDate.text = str(startDate)
        
    finishDate = tree.find("./gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod/gml:endPosition", namespaces)
    finishDate.text = str(endDate)
        
    return tree

def getS411ExchangeCatalogueFromTemplate(templateFilePath, metadataTree, exchangeSetName, datasetName, extent, datasetPath):
    tree = ET.parse(templateFilePath)
    
    ET.register_namespace("gsr", "http://www.isotc211.org/2005/gsr")
    ET.register_namespace("gco", "http://www.isotc211.org/2005/gco")
    ET.register_namespace("gmd", "http://www.isotc211.org/2005/gmd")
    ET.register_namespace("gts", "http://www.isotc211.org/2005/gts")
    ET.register_namespace("gss", "http://www.isotc211.org/2005/gss")
    ET.register_namespace("gml", "http://www.opengis.net/gml/3.2")
    ET.register_namespace("ec", "http://www.iho.int/S100EC")
    
        
    namespaces = {"gsr": "http://www.isotc211.org/2005/gsr", 
                  "gco": "http://www.isotc211.org/2005/gco",
                  "gmd": "http://www.isotc211.org/2005/gmd",  
                  "gts": "http://www.isotc211.org/2005/gts",
                  "gss": "http://www.isotc211.org/2005/gss",
                  "gml": "http://www.opengis.net/gml/3.2",
                  "ec" : "http://www.iho.int/S100EC"}
    
    identifier = tree.find("./ec:identifier/ec:identifier", namespaces)
    identifier.text = str(exchangeSetName)
    
    date = tree.find("./ec:identifier/ec:date/gco:Date", namespaces)
    mdDate = metadataTree.find("./gmd:dateStamp/gco:Date", namespaces).text
    date.text = str(mdDate)
    
    dsFileName = tree.find("./ec:S100_DatasetDiscoveryMetadata/ec:fileName", namespaces)
    mdDsFileName = metadataTree.find("./gmd:fileIdentifier/gco:CharacterString", namespaces).text
    dsFileName.text = str(mdDsFileName) + ".gml"
    
    # Relative path to exchange set root
    dsFilePath = tree.find("./ec:S100_DatasetDiscoveryMetadata/ec:filePath", namespaces)
    dsFilePath.text = "/data/" + str(mdDsFileName + ".gml")
    
    bboxElement = metadataTree.find("./gmd:identificationInfo/gmd:extent/gmd:/EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox", namespaces)
    ecBbox = tree.find("./ec:S100_DatasetDiscoveryMetadata/ec:boundingBox", namespaces)
    ET.SubElement(ecBbox, bboxElement)
    
    
    bbPolygon = tree.find("./ec:S100_DatasetDiscoveryMetadata/ec:boundingPolygon/gmd:EX_BoundingPolygon/gmd:polygon/gml:Polygon", namespaces)
    bbPolygon.attrib["gml:id"] = exchangeSetName + "g"
    
    
    maxX = str(extent[0])
    minX = str(extent[1])
    maxY = str(extent[2])
    minY = str(extent[3])
    
    posList = minX + " " + minY + " " + minX + " " + maxY + " " + maxX + " " + maxY + " " + maxX + " " + minY + " " + minX + " " + minY
    bbPolygonPosList = tree.find("./ec:S100_DatasetDiscoveryMetadata/ec:boundingPolygon/gmd:EX_BoundingPolygon/gmd:polygon/gml:Polygon/gml:exterior/gml:LinearRing/gml:posList", namespaces)
    bbPolygonPosList.text = posList
    
    checksum = str(util.calculateCRCCode(datasetPath))
    checksumElement = tree.find("./ec:S100_DatasetDiscoveryMetadata/ec:cyclicRedundancyCheckSum", namespaces)
    checksumElement.text = checksum
    
    return tree
        
#md = S411Metadata("idd1")
#md.getS411MetadataFromTemplate("mdTemplateBshBaltic.xml", "id1",dateStamp="2014-02-12", extent=[23,45,23,56], startDate="2014-4-4", endDate="2014-4-4")   






class S411Metadata(object):
    def __init__(self, fileId):
        
        self.fileId = fileId  # mandatory
        
        
        # gmd language element
        self.languageCodeList = "http://www.isotc211.org/2005/resources/Codelist/ML_gmxCodelists.xml#LanguageCode"
        self.languageCodeListValue = "eng"
        self.languageCodeListValueFull = "English"
        
        # gmd characterSet element
        self.characterSetCodeList = "http://www.isotc211.org/2005/resources/Codelist/ML_gmxCodelists.xml#MD_CharacterSetCode"
        self.characterSetCodeListValue = "utf8"
        self.characterSetCodeListValueFull = "UTF 8"
        
        # gmd contact El
        self.individualName = ""
        self.organisationName = ""
        self.phone = ""
        self.fax = ""
        self.streetAndHouseNr = ""
        self.city = ""
        self.zip = ""
        self.email = ""
        
        self.roleCodeList = "http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_RoleCode"
        self.roleCodeListValue = "originator"
        self.roleCodeListValueFull = "originator"
        
        # gmd DateStamp element
        self.dateStamp = ""
        
        # gmd Data Identification element
        self.idTitle = ""
        
        self.idDate = ""
        self.idDateTypeCodeList = "http://www.isotc211.org/2005/resources/Codelist/ML_gmxCodelists.xml#CI_DateTypeCode"
        self.idDateTypeCodeListValue = "creation"
        self.idDateTypeCodeListValueFull = "creation"
        self.idAbstract = ""
        
        self.idLanguageCodeList = "http://www.isotc211.org/2005/resources/Codelist/ML_gmxCodelists.xml#LanguageCode"
        self.idLanguageCodeListValue = "eng"
        self.idLanguageCodeListValueFull = "English"
        
        self.IdCharacterSetCodeList = "http://www.isotc211.org/2005/resources/Codelist/ML_gmxCodelists.xml#MD_CharacterSetCode"
        self.IdCharacterSetCodeListValue = "utf8"
        self.IdCharacterSetCodeListValueFull = "UTF 8"
        
        self.idTopicCategory = "geoscientificInformation"
        
        self.extentMinX = ""
        self.extentMaxX = ""
        self.extentMinY = ""
        self.extentMaxY = ""
        
        self.startDate = ""
        self.endDate = ""

    def get_role_code_list(self):
        return self.__roleCodeList


    def set_role_code_list(self, value):
        self.__roleCodeList = value


    def get_role_code_list_value(self):
        return self.__roleCodeListValue


    def get_role_code_list_value_full(self):
        return self.__roleCodeListValueFull


    def set_role_code_list_value(self, value):
        self.__roleCodeListValue = value


    def set_role_code_list_value_full(self, value):
        self.__roleCodeListValueFull = value

    def get_file_id(self):
        return self.__fileId


    def get_language_code_list(self):
        return self.__languageCodeList


    def get_language_code_list_value(self):
        return self.__languageCodeListValue


    def get_language_code_list_value_full(self):
        return self.__languageCodeListValueFull


    def get_character_set_code_list(self):
        return self.__characterSetCodeList


    def get_character_set_code_list_value(self):
        return self.__characterSetCodeListValue


    def get_character_set_code_list_value_full(self):
        return self.__characterSetCodeListValueFull


    def get_individual_name(self):
        return self.__individualName


    def get_organisation_name(self):
        return self.__organisationName


    def get_phone(self):
        return self.__phone


    def get_fax(self):
        return self.__fax


    def get_street_and_house_nr(self):
        return self.__streetAndHouseNr


    def get_city(self):
        return self.__city


    def get_zip(self):
        return self.__zip


    def get_email(self):
        return self.__email


    def get_role(self):
        return self.__role


    def get_date_stamp(self):
        return self.__dateStamp


    def get_id_title(self):
        return self.__idTitle


    def get_id_date(self):
        return self.__idDate


    def get_id_date_type_code_list(self):
        return self.__idDateTypeCodeList


    def get_id_date_type_code_list_value(self):
        return self.__idDateTypeCodeListValue


    def get_id_date_type_code_list_value_full(self):
        return self.__idDateTypeCodeListValueFull


    def get_id_abstract(self):
        return self.__idAbstract


    def get_id_language_code_list(self):
        return self.__idLanguageCodeList


    def get_id_language_code_list_value(self):
        return self.__idLanguageCodeListValue


    def get_id_language_code_list_value_full(self):
        return self.__idLanguageCodeListValueFull


    def get_id_character_set_code_list(self):
        return self.__IdCharacterSetCodeList


    def get_id_character_set_code_list_value(self):
        return self.__IdCharacterSetCodeListValue


    def get_id_character_set_code_list_value_full(self):
        return self.__IdCharacterSetCodeListValueFull


    def get_id_topic_category(self):
        return self.__idTopicCategory


    def get_extent_min_x(self):
        return self.__extentMinX


    def get_extent_max_x(self):
        return self.__extentMaxX


    def get_extent_min_y(self):
        return self.__extentMinY


    def get_extent_max_y(self):
        return self.__extentMaxY


    def get_start_date(self):
        return self.__startDate


    def get_end_date(self):
        return self.__endDate


    def set_file_id(self, value):
        self.__fileId = value


    def set_language_code_list(self, value):
        self.__languageCodeList = value


    def set_language_code_list_value(self, value):
        self.__languageCodeListValue = value


    def set_language_code_list_value_full(self, value):
        self.__languageCodeListValueFull = value


    def set_character_set_code_list(self, value):
        self.__characterSetCodeList = value


    def set_character_set_code_list_value(self, value):
        self.__characterSetCodeListValue = value


    def set_character_set_code_list_value_full(self, value):
        self.__characterSetCodeListValueFull = value


    def set_individual_name(self, value):
        self.__individualName = value


    def set_organisation_name(self, value):
        self.__organisationName = value


    def set_phone(self, value):
        self.__phone = value


    def set_fax(self, value):
        self.__fax = value


    def set_street_and_house_nr(self, value):
        self.__streetAndHouseNr = value


    def set_city(self, value):
        self.__city = value


    def set_zip(self, value):
        self.__zip = value


    def set_email(self, value):
        self.__email = value


    def set_role(self, value):
        self.__role = value


    def set_date_stamp(self, value):
        self.__dateStamp = value


    def set_id_title(self, value):
        self.__idTitle = value


    def set_id_date(self, value):
        self.__idDate = value


    def set_id_date_type_code_list(self, value):
        self.__idDateTypeCodeList = value


    def set_id_date_type_code_list_value(self, value):
        self.__idDateTypeCodeListValue = value


    def set_id_date_type_code_list_value_full(self, value):
        self.__idDateTypeCodeListValueFull = value


    def set_id_abstract(self, value):
        self.__idAbstract = value


    def set_id_language_code_list(self, value):
        self.__idLanguageCodeList = value


    def set_id_language_code_list_value(self, value):
        self.__idLanguageCodeListValue = value


    def set_id_language_code_list_value_full(self, value):
        self.__idLanguageCodeListValueFull = value


    def set_id_character_set_code_list(self, value):
        self.__IdCharacterSetCodeList = value


    def set_id_character_set_code_list_value(self, value):
        self.__IdCharacterSetCodeListValue = value


    def set_id_character_set_code_list_value_full(self, value):
        self.__IdCharacterSetCodeListValueFull = value


    def set_id_topic_category(self, value):
        self.__idTopicCategory = value


    def set_extent_min_x(self, value):
        self.__extentMinX = value


    def set_extent_max_x(self, value):
        self.__extentMaxX = value


    def set_extent_min_y(self, value):
        self.__extentMinY = value


    def set_extent_max_y(self, value):
        self.__extentMaxY = value


    def set_start_date(self, value):
        self.__startDate = value


    def set_end_date(self, value):
        self.__endDate = value

    
    # create XML Tree with data
    def createXmlTree(self, S411Md):
        #S411Md = S411Metadata()
        #S411Md = MdObject
        
        ET.register_namespace("gmd", "http://www.isotc211.org/2005/gmd")
        ET.register_namespace("gco", "http://www.isotc211.org/2005/gco")
        ET.register_namespace("gml", "http://www.opengis.net/gml/3.2")
        
        root = ET.Element("{http://www.isotc211.org/2005/gmd}MD_Metadata")
        
        # file Identifier
        fileIdEl = ET.SubElement(root, "{http://www.isotc211.org/2005/gmd}fileIdentifier")
        fileIdStringEl = ET.SubElement(fileIdEl, "{http://www.isotc211.org/2005/gco}String")
        fileIdStringEl.text = str(S411Md.get_file_id())
        
        # language
        langEl = ET.SubElement(root, "{http://www.isotc211.org/2005/gmd}language")
        langCodeEl = ET.SubElement(langEl, "{http://www.isotc211.org/2005/gmd}LanguageCode")
        langCodeEl.attrib["codeList"] = str(S411Md.get_language_code_list())
        langCodeEl.attrib["codeListValue"] = str(S411Md.get_language_code_list_value())
        langCodeEl.text = str(S411Md.get_language_code_list_value_full())
        
        # character set
        charSetEl = ET.SubElement(root, "{http://www.isotc211.org/2005/gmd}characterSet")
        md_charSetCodeEl = ET.SubElement(charSetEl, "{http://www.isotc211.org/2005/gmd}MD_CharacterSetCode")
        md_charSetCodeEl.attrib["codeList"] = str(S411Md.get_character_set_code_list())
        md_charSetCodeEl.attrib["codeListValue"] = str(S411Md.get_character_set_code_list_value())
        md_charSetCodeEl.text = str(S411Md.get_character_set_code_list_value_full())
        
        # contact
        contactEl = ET.SubElement(root, "{http://www.isotc211.org/2005/gmd}contact")
        ci_responsiblePartyEl = ET.SubElement(contactEl, "{http://www.isotc211.org/2005/gmd}CI_ResponsibleParty")
        
        
        individualNameEl = ET.SubElement(ci_responsiblePartyEl, "{http://www.isotc211.org/2005/gmd}individualName")
        individualNameStringEl = ET.SubElement(individualNameEl, "{http://www.isotc211.org/2005/gco}String")
        individualNameStringEl.text = str(S411Md.get_individual_name())
        
        
        organisationNameEl = ET.SubElement(ci_responsiblePartyEl, "{http://www.isotc211.org/2005/gmd}organisationName")
        organisationNameStringEl = ET.SubElement(organisationNameEl, "{http://www.isotc211.org/2005/gco}String")
        organisationNameStringEl.text = str(S411Md.get_organisation_name())
        
        
        contactInfoEl = ET.SubElement(ci_responsiblePartyEl, "{http://www.isotc211.org/2005/gmd}contactInfo")
        ci_contactEl = ET.SubElement(contactInfoEl, "{http://www.isotc211.org/2005/gmd}CI_Contact")
        
        ci_contactPhoneEl = ET.SubElement(ci_contactEl, "{http://www.isotc211.org/2005/gmd}phone")
        ci_contactPhoneCi_TelephoneEl = ET.SubElement(ci_contactPhoneEl, "{http://www.isotc211.org/2005/gmd}CI_Telephone")
        ci_contactPhoneCi_TelephoneVoiceEl = ET.SubElement(ci_contactPhoneCi_TelephoneEl, "{http://www.isotc211.org/2005/gmd}voice")
        ci_contactPhoneCi_TelephoneVoiceStringEl = ET.SubElement(ci_contactPhoneCi_TelephoneVoiceEl, "{http://www.isotc211.org/2005/gco}String")
        ci_contactPhoneCi_TelephoneVoiceStringEl.text = str(S411Md.get_phone())
        ci_contactPhoneCi_TelephoneFacsimileEl = ET.SubElement(ci_contactPhoneCi_TelephoneEl, "{http://www.isotc211.org/2005/gmd}facsimile")
        ci_contactPhoneCi_TelephoneFacsimileStringEl = ET.SubElement(ci_contactPhoneCi_TelephoneFacsimileEl, "{http://www.isotc211.org/2005/gco}String")
        ci_contactPhoneCi_TelephoneFacsimileStringEl.text = str(S411Md.get_fax())
        
        ci_contactAddressEl = ET.SubElement(ci_contactEl, "{http://www.isotc211.org/2005/gmd}address")
        ci_contactAddressCi_AddressEl = ET.SubElement(ci_contactAddressEl, "{http://www.isotc211.org/2005/gmd}CI_Address")
        ci_contactAddressCi_AddressDeliveryPointEl = ET.SubElement(ci_contactAddressCi_AddressEl, "{http://www.isotc211.org/2005/gmd}deliveryPoint")
        ci_contactAddressCi_AddressDeliveryPointString = ET.SubElement(ci_contactAddressCi_AddressDeliveryPointEl, "{http://www.isotc211.org/2005/gco}String")
        ci_contactAddressCi_AddressDeliveryPointString.text = str(S411Md.get_street_and_house_nr())
        ci_contactAddressCi_AddressAdministrativeAreaEl = ET.SubElement(ci_contactAddressCi_AddressEl, "{http://www.isotc211.org/2005/gmd}administrativeArea")
        ci_contactAddressCi_AddressAdministrativeAreaStringEl = ET.SubElement(ci_contactAddressCi_AddressAdministrativeAreaEl, "{http://www.isotc211.org/2005/gco}String")
        ci_contactAddressCi_AddressAdministrativeAreaStringEl.text = str(S411Md.get_city())
        ci_contactAddressCi_AddressPostalCodeEl = ET.SubElement(ci_contactAddressCi_AddressEl, "{http://www.isotc211.org/2005/gmd}postalCode")
        ci_contactAddressCi_AddressPostalCodeStringEl = ET.SubElement(ci_contactAddressCi_AddressPostalCodeEl, "{http://www.isotc211.org/2005/gco}String")
        ci_contactAddressCi_AddressPostalCodeStringEl.text = str(S411Md.get_zip())
        ci_contactAddressCi_AddressElectronicMailAddressEl = ET.SubElement(ci_contactAddressCi_AddressEl, "{http://www.isotc211.org/2005/gmd}electronicMailAddress")
        ci_contactAddressCi_AddressElectronicMailAddressStringEl = ET.SubElement(ci_contactAddressCi_AddressElectronicMailAddressEl, "{http://www.isotc211.org/2005/gco}String")
        ci_contactAddressCi_AddressElectronicMailAddressStringEl.text = str(S411Md.get_email())
        
        roleEl = ET.SubElement(ci_responsiblePartyEl, "{http://www.isotc211.org/2005/gmd}role")
        roleCi_RoleCodeEl = ET.SubElement(roleEl, "{http://www.isotc211.org/2005/gmd}CI_RoleCode")
        roleCi_RoleCodeEl.attrib["codeList"] = str(S411Md.get_role_code_list())
        roleCi_RoleCodeEl.attrib["codeListValue"] = str(S411Md.get_role_code_list_value())
        roleCi_RoleCodeEl.text = str(S411Md.get_role_code_list_value_full())
    
        # Date Stamp
        dateStampEl = ET.SubElement(root, "{http://www.isotc211.org/2005/gmd}dateStamp")
        dateStamppDateEl = ET.SubElement(dateStampEl, "{http://www.isotc211.org/2005/gco}Date")
        dateStamppDateEl.text = str(S411Md.get_date_stamp())
        
        # Identification Info
        idInfoEl = ET.SubElement(root, "{http://www.isotc211.org/2005/gmd}identificationInfo")
        MD_DataIdEl = ET.SubElement(idInfoEl, "{http://www.isotc211.org/2005/gmd}MD_DataIdentification")
        
        Md_DataId_CitationEl = ET.SubElement(MD_DataIdEl, "{http://www.isotc211.org/2005/gmd}citation")
        Md_DataId_CI_CitationEl = ET.SubElement(Md_DataId_CitationEl, "{http://www.isotc211.org/2005/gmd}CI_Citation")
        
        Md_DataId_CI_Citation_TitleEl = ET.SubElement(Md_DataId_CI_CitationEl, "{http://www.isotc211.org/2005/gmd}title")
        Md_DataId_CI_Citation_TitleStringEl = ET.SubElement(Md_DataId_CI_Citation_TitleEl, "{http://www.isotc211.org/2005/gco}CharacterString")
        Md_DataId_CI_Citation_TitleStringEl.text = str(S411Md.get_id_title())
        
        Md_DataId_CI_Citation_DateEl = ET.SubElement(Md_DataId_CI_CitationEl, "{http://www.isotc211.org/2005/gmd}date")
        Md_DataId_CI_Citation_Date_CI_DateEl = ET.SubElement(Md_DataId_CI_Citation_DateEl, "{http://www.isotc211.org/2005/gmd}CI_Date")
        Md_DataId_CI_Citation_Date_CI_Date_DateEl = ET.SubElement(Md_DataId_CI_Citation_Date_CI_DateEl, "{http://www.isotc211.org/2005/gmd}date")
        Md_DataId_CI_Citation_Date_CI_Date_Date_GcoDateEl = ET.SubElement(Md_DataId_CI_Citation_Date_CI_Date_DateEl, "{http://www.isotc211.org/2005/gco}Date")
        Md_DataId_CI_Citation_Date_CI_Date_Date_GcoDateEl.text = str(S411Md.get_id_date())
        
        Md_DataId_CI_Citation_Date_CI_Date_DateTypeEl = ET.SubElement(Md_DataId_CI_Citation_Date_CI_DateEl, "{http://www.isotc211.org/2005/gmd}dateType")
        Md_DataId_CI_Citation_Date_CI_Date_DateType_CI_DateTypeEl = ET.SubElement(Md_DataId_CI_Citation_Date_CI_Date_DateTypeEl, "{http://www.isotc211.org/2005/gmd}CI_DateType")
        Md_DataId_CI_Citation_Date_CI_Date_DateType_CI_DateTypeEl.attrib["codeList"] = str(S411Md.get_id_date_type_code_list())
        Md_DataId_CI_Citation_Date_CI_Date_DateType_CI_DateTypeEl.attrib["codeListValue"] = str(S411Md.get_id_date_type_code_list_value())
        Md_DataId_CI_Citation_Date_CI_Date_DateType_CI_DateTypeEl.text = str(S411Md.get_id_date_type_code_list_value_full())
        
        Md_DataId_AbstractEl = ET.SubElement(MD_DataIdEl, "{http://www.isotc211.org/2005/gmd}abstract")
        Md_DataId_AbstractStringEl = ET.SubElement(Md_DataId_AbstractEl, "{http://www.isotc211.org/2005/gco}CharacterString")
        Md_DataId_AbstractStringEl.text = str(S411Md.get_id_abstract())      
        
        
        Md_DataId_LangEl = ET.SubElement(MD_DataIdEl, "{http://www.isotc211.org/2005/gmd}language")
        Md_DataId_LangCodeEl = ET.SubElement(Md_DataId_LangEl, "{http://www.isotc211.org/2005/gmd}LanguageCode")
        Md_DataId_LangCodeEl.attrib["codeList"] = str(S411Md.get_id_language_code_list())
        Md_DataId_LangCodeEl.attrib["codeListValue"] = str(S411Md.get_id_language_code_list_value())
        Md_DataId_LangCodeEl.text = str(S411Md.get_id_language_code_list_value_full())
        
        
        Md_DataId_charSetEl = ET.SubElement(MD_DataIdEl, "{http://www.isotc211.org/2005/gmd}characterSet")
        Md_DataId_charSet_Md_CharSetCodeEl = ET.SubElement(Md_DataId_charSetEl, "{http://www.isotc211.org/2005/gmd}Md_CharacterSetCode")
        Md_DataId_charSet_Md_CharSetCodeEl.attrib["codeList"] = str(S411Md.get_id_character_set_code_list())
        Md_DataId_charSet_Md_CharSetCodeEl.attrib["codeListValue"] = str(S411Md.get_id_character_set_code_list_value())
        Md_DataId_charSet_Md_CharSetCodeEl.text = str(S411Md.get_id_character_set_code_list_value_full())
        
        
        Md_DataId_topicCategoryEl = ET.SubElement(MD_DataIdEl, "{http://www.isotc211.org/2005/gmd}topicCategory")
        Md_DataId_TopicCategoryCodeEl = ET.SubElement(Md_DataId_topicCategoryEl, "{http://www.isotc211.org/2005/gmd}MD_TopicCategoryCode")
        Md_DataId_TopicCategoryCodeEl.text = str(S411Md.get_id_topic_category())
        
        
        Md_DataId_ExtentEl   = ET.SubElement(MD_DataIdEl, "{http://www.isotc211.org/2005/gmd}extent")
        Md_DataId_EX_ExtentEl = ET.SubElement(Md_DataId_ExtentEl, "{http://www.isotc211.org/2005/gmd}EX_Extent")
        
        Md_DataId_EX_Extent_GeographicElementEl = ET.SubElement(Md_DataId_EX_ExtentEl, "{http://www.isotc211.org/2005/gmd}geographicElement")
        EX_GeographicBBoxEl = ET.SubElement(Md_DataId_EX_Extent_GeographicElementEl, "{http://www.isotc211.org/2005/gmd}geographicBoundingBox")
        westBoundLongitudeEl = ET.SubElement(EX_GeographicBBoxEl, "{http://www.isotc211.org/2005/gmd}westBoundLongitude")
        westBoundLongitudeDecimalEl = ET.SubElement(westBoundLongitudeEl, "{http://www.isotc211.org/2005/gco}Decimal")
        westBoundLongitudeDecimalEl.text = str(S411Md.get_extent_min_x())
        
        eastBoundLongitudeEl = ET.SubElement(EX_GeographicBBoxEl, "{http://www.isotc211.org/2005/gmd}eastBoundLongitude")
        eastBoundLongitudeDecimalEl = ET.SubElement(eastBoundLongitudeEl, "{http://www.isotc211.org/2005/gco}Decimal")
        eastBoundLongitudeDecimalEl.text = str(S411Md.get_extent_max_x())
        
        southBoundLatitudeEl = ET.SubElement(EX_GeographicBBoxEl, "{http://www.isotc211.org/2005/gmd}southBoundLatitude")
        southBoundLatitudeElDecimalEl = ET.SubElement(southBoundLatitudeEl, "{http://www.isotc211.org/2005/gco}Decimal")
        southBoundLatitudeElDecimalEl.text = str(S411Md.get_extent_min_y())
        
        northBoundLatitudeEl = ET.SubElement(EX_GeographicBBoxEl, "{http://www.isotc211.org/2005/gmd}northBoundLatitude")
        northBoundLatitudeElDecimalEl = ET.SubElement(northBoundLatitudeEl, "{http://www.isotc211.org/2005/gco}Decimal")
        northBoundLatitudeElDecimalEl.text = str(S411Md.get_extent_min_y())
        
        
        Md_DataId_EX_Extent_TemporalElement = ET.SubElement(Md_DataId_EX_ExtentEl, "{http://www.isotc211.org/2005/gmd}temporalElement")
        EX_TempExtentEl = ET.SubElement(Md_DataId_EX_Extent_TemporalElement, "{http://www.isotc211.org/2005/gmd}EX_TemporalExtent")
        EX_TempExtent_extentEl = ET.SubElement(EX_TempExtentEl, "{http://www.isotc211.org/2005/gmd}extent")
        GML_TimePeriodEl = ET.SubElement(EX_TempExtent_extentEl, "{http://www.opengis.net/gml/3.2}TimePeriod")
        GML_BeginTimePositionEl = ET.SubElement(GML_TimePeriodEl, "{http://www.opengis.net/gml/3.2}beginPosition")
        GML_BeginTimePositionEl.text = str(S411Md.get_start_date())
        GML_EndTimePositionEl = ET.SubElement(GML_TimePeriodEl, "{http://www.opengis.net/gml/3.2}endPosition") 
        GML_EndTimePositionEl.text = str(S411Md.get_end_date())
        
        
        tree = ET.ElementTree(root)
        
        return tree
    
    # create S411 Metadata Object from XML Template file, can be configured
    # params "extent" is a list of coordinates {minX, maxX, minY, maxY}, start and end dates describes valid time period
