from requests import get
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as et
import xmltodict
import json


url = "http://www.cbr.ru/scripts/XML_valFull.asp"
response = get(url).content
root = ET.fromstring(response)

to_string  = et.tostring(root, encoding='UTF-8', method='xml')

xml_to_dict = xmltodict.parse(to_string)

with open("data_file.json", "w",) as json_file:
    json.dump(xml_to_dict, json_file, indent = 2)