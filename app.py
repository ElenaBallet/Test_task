from requests import get
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import datetime


def code(Char_Code, date_1, date_2):
    with open('data_file.json') as f:
        data_file = json.load(f)
    date1 = (datetime.datetime.strptime(str(date_1), '%Y-%m-%d')).strftime('%d/%m/%Y')
    date2 = (datetime.datetime.strptime(str(date_2), '%Y-%m-%d')).strftime('%d/%m/%Y')
    ID = search_dictionaries("ISO_Char_Code", Char_Code, data_file)
    Value = value_currency(date1, date2, ID)
    diff_value = {
        date_1: Value[0],
        date_2: Value[1],
        'difference_value': Value[2]
    }
    return diff_value


def search_dictionaries(key, value, list_of_dictionaries):
    return [element["ParentCode"] for element in list_of_dictionaries if element[key] == value][0]


def value_currency(date_one, date_two, id_currency):
    url = f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={date_one}&date_req2={date_two}&VAL_NM_RQ={id_currency}"
    response = get(url).content
    root = ET.fromstring(response)
    
    d_one = (datetime.datetime.strptime(str(date_one), '%d/%m/%Y')).strftime('%d.%m.%Y')
    d_two = (datetime.datetime.strptime(str(date_two), '%d/%m/%Y')).strftime('%d.%m.%Y')

    i = 0
    value_one = ''
    value_two = ''
    for child in root:
        if child.attrib['Date'] == d_one:
            value_one = root[i][1].text
        
        if child.attrib['Date'] == d_two:
            value_two = root[i][1].text

        i=+1

    diff = float(value_two.replace(',', '.')) - float(value_one.replace(',', '.'))
    difference = float('{:.3f}'.format(diff))

    return  value_one, value_two, difference