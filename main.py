from fastapi.responses import JSONResponse
from fastapi import FastAPI
import json
from datetime import date
from app import code


app = FastAPI()


@app.get("/")
def get_titles():
    return JSONResponse({"status":"OK"})


@app.get("/date")
async def get_two_date(
    date_1: date,
    date_2: date,
    Char_Code: str
):

    return code(Char_Code, date_1,date_2)


@app.get("/get_currency_list")
async def get_currency_list():
    """get full list currency"""
    with open("data_file.json") as js:
        data = json.load(js)
    return data