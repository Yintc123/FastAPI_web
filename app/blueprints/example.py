# from flask import Blueprint
from typing import Optional
from fastapi import *
from app.database.db import Order, Customer, Product, db_session
from pydantic import BaseModel

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
    
    customer = db_session.query(Customer).filter(Customer.customer_name==name).all()
    if not customer:
        print(customer)
        customer=Customer(customer_name=name)
        db_session.add(customer)
        db_session.commit()
        db_session.close()

    return 'welcome to post test'

# 修改一筆訂單
url_modify_order='/order/modify'
@api_page.patch(url_modify_order)
def modify_order():
    return 'welcome to patch test'
