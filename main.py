from fastapi.responses import JSONResponse
from fastapi import FastAPI
import json
from datetime import date
from get_difference_in_course import difference_in_course

app = FastAPI()

# главная страница сайта
@app.get("/")
def get_titles():
    return JSONResponse({"status": "OK"})

# получение курса валют за первую и вторую даты, получение разницы курса валют
@app.get("/date")
async def get_two_date(
    date_1: date, # дата принимается в формате: YYYY-mm-dd
    date_2: date, # дата принимается в формате: YYYY-mm-dd
    Char_Code: str, #  символ валюты принимается в формате строки
):
    return difference_in_course(Char_Code, date_1, date_2) # import difference_in_course из файла get_difference_in_course

# получение списка валют из файла data_file.json
@app.get("/get_currency_list")
async def get_currency_list():
    """get full list currency"""
    with open("data_file.json") as js:
        data = json.load(js)
    return data