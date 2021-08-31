from requests import get
import json
import xml.etree.ElementTree as ET


def code(Char_Code, date_1, date_2):
    with open('data_file.json') as f:
        data_file = json.load(f)
    ID = search_dictionaries("ISO_Char_Code", Char_Code, data_file)
    Value = value_currency(date_1, date_2, ID)
    return Value


def search_dictionaries(key, value, list_of_dictionaries):
    return [element["ParentCode"] for element in list_of_dictionaries if element[key] == value][0]


def value_currency(date_one, date_two, id_currency):
    url = f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2001&date_req2=14/03/2001&VAL_NM_RQ={id_currency}"
    response = get(url).content
    root = ET.fromstring(response)

    i = 0
    for child in root:
        if child.attrib['Date'] == date_one:
            date_one = root[i][1].text

        
        if child.attrib['Date'] == date_two:
            date_two = root[i][1].text

        i=+1

    return date_one, date_two
