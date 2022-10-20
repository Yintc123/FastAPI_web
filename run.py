# from flask import Blueprint
import uvicorn
from app import app, templates
from fastapi import *
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    context={"request":request}
    return templates.TemplateResponse("index.html", context)

@app.get("/orders", response_class=HTMLResponse)
def index(request:Request):
    context={"request":request}
    return templates.TemplateResponse("orders.html", context)

@app.get("/order", response_class=HTMLResponse)
def index(request:Request):
    context={"request":request}
    return templates.TemplateResponse("modify_order_page.html", context)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    uvicorn.run(app, host='127.0.0.1', port=6060)
    