# from flask import Blueprint
import uvicorn
import os
from dotenv import load_dotenv, find_dotenv
from app import app, templates
from fastapi import *
from fastapi.responses import HTMLResponse

# 使用 .env 檔的資料
load_dotenv(find_dotenv())
env=os.getenv('MODE')

# 路由：首頁（新增訂單頁面）
@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    context={"request":request}
    return templates.TemplateResponse("index.html", context)

# 路由：訂單總攬頁面
@app.get("/orders", response_class=HTMLResponse)
def index(request:Request):
    context={"request":request}
    return templates.TemplateResponse("orders.html", context)

# 路由：查詢訂單頁面
@app.get("/order", response_class=HTMLResponse)
def index(request:Request):
    context={"request":request}
    return templates.TemplateResponse("modify_order_page.html", context)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    uvicorn.run(app, host=os.getenv('host_'+env), port=6060)
    