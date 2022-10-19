# from flask import Blueprint
from typing import Optional
from fastapi import *
from app.database.db import Order, db_session
from pydantic import BaseModel

class Order_Model(BaseModel):
    order_id: Optional[int]
    name: str
    product_name: str
    amount: int
    price: int

# api_page = Blueprint('Api', __name__)

# @api_page.route('/endpoint1', methods=['GET'])
# def getAdsData():
#     return 'welcome to test'

api_page = APIRouter()

@api_page.get('/endpoint1')
def getAdsData():
    return 'welcome to test'

# 新增一筆訂單
url_add_order='/order/add'
@api_page.post(url_add_order)
def create_order(order:Order_Model):

    for i in order:
        print(i)
    # order=Order(customer_name='Tom', customer_id=0)
    # db_session.add(order)
    # db_session.commit()
    # db_session.close()

    return 'welcome to post test'

# 修改一筆訂單
url_modify_order='/order/modify'
@api_page.patch(url_modify_order)
def modify_order():
    return 'welcome to patch test'
