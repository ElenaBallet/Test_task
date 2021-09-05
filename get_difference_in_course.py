from requests import get
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import datetime


# функция возвращает значения курса валют за первую и вторую даты и сами даты в формате YYYY-mm-dd, разницу курса за первую и вторую даты. Полученные данные возвращаются в файл main
def difference_in_course(Char_Code, date_1, date_2): # данные из файла main
    with open('data_file.json') as f:
        data_file = json.load(f)
    date1 = (datetime.datetime.strptime(str(date_1), '%Y-%m-%d')).strftime('%d/%m/%Y') # приводим даты к ввиду dd/mm/YYYY, чтобы потом передать в url
    date2 = (datetime.datetime.strptime(str(date_2), '%Y-%m-%d')).strftime('%d/%m/%Y') # приводим даты к ввиду dd/mm/YYYY, чтобы потом передать в url
    ID = id_currency("ISO_Char_Code", Char_Code, data_file)
    Value = value_currency(date1, date2, ID)
    diff_value = {
        date_1: Value[0],
        date_2: Value[1],
        'difference_value': Value[2]
    }
    return diff_value

# функция возвращает ID валюты из файла data_file. ID находим по символу валюты, который ввел пользователь
def id_currency(key, value, list):
     return [element["ParentCode"] for element in list if element[key] == value][0]

# функция возвращает значения курса валют за первую и вторую даты, разницу курса за первую и вторую даты
def value_currency(date_one, date_two, id_currency):
    url = f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={date_one}&date_req2={date_two}&VAL_NM_RQ={id_currency}" # по полученным датам от пользователи и ID валюты находим нужный url
    response = get(url).content
    root = ET.fromstring(response)
    
    value_one = root[0][1].text # получаем значение валюты за первую дату
    value_two = root[len(root) - 1][1].text # получаем значение валюты за вторую дату

    diff = float(value_two.replace(',', '.')) - float(value_one.replace(',', '.')) # получаем разницу значений за первую и вторую даты
    difference = float('{:.3f}'.format(diff)) # у занчения валюты оставляем три знака после запятой

    return  value_one, value_two, difference