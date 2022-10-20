# from flask import Blueprint
from typing import Optional
from fastapi import *
from pydantic import BaseModel
from app.database.order_db import Order_db

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

api_page = APIRouter()

@api_page.get('/endpoint1')
def getAdsData():
    return 'welcome to test'

# 新增一筆訂單
url_add_order='/order/add'
@api_page.post(url_add_order)
def create_order(name : str = Form(...), product_name : str = Form(...), price: int = Form(...), amount: int = Form(...)):

    print(name)
    print(product_name)
    print(price)
    print(amount)

    order = Order_db().create_order(name, product_name, price, amount)
    print(order)

    return 'welcome to post test'

# 修改一筆訂單
url_modify_order='/order/modify'
@api_page.patch(url_modify_order)
def modify_order():
    return 'welcome to patch test'
