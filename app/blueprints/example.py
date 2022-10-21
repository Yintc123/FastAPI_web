# from flask import Blueprint
from typing import Optional
from fastapi import *
from numpy import product
from pydantic import BaseModel
from app.database.order_db import Order_db
import asyncio

# api_page = Blueprint('Api', __name__)

# @api_page.route('/endpoint1', methods=['GET'])
# def getAdsData():
#     return 'welcome to test'

class Order_Model(BaseModel):
    order_id: Optional[int]
    name: str
    product_name: str
    amount: int
    price: int
    total: int

api_page = APIRouter()

@api_page.get('/endpoint1')
def getAdsData():
    return 'welcome to test'

# 查詢特定訂單
url_order='/order/{order_id}'
@api_page.get(url_order)
async def get_orders(order_id:int):
    order = await asyncio.create_task(Order_db().get_order(order_id))
    return order

# 查詢所有訂單
@api_page.get('/orders')
async def get_orders():
    orders = await Order_db().get_orders()
    return orders

# 新增一筆訂單
url_add_order='/order'
@api_page.post(url_add_order)
async def create_order(name : str = Form(...), product_name : str = Form(...), price: int = Form(...), amount: int = Form(...)):

    if not name or not product_name or not price or not amount:
        return {"error":"請填寫完整資訊"}

    order = await Order_db().create_order(name, product_name, price, amount)

    return {"ok":200}

# 修改一筆訂單
@api_page.patch(url_order)
async def modify_order(order_id: int, name : str = Form(...), product_name : str = Form(...), price: int = Form(...), amount: int = Form(...)):
    order = await Order_db().modify_order(name, product_name, price, amount, order_id)
    return {"ok":200}