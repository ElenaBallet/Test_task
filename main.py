from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_titles():
    return JSONResponse({"status":"OK"})


@app.get("/items/{item_id}")
def difference_in_quotes(item_id: int, q: Optional[str] = None):
    return JSONResponse({"status":"OK"})