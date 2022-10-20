from .db import db_session, Order
from .customer_db import Customer_db
from .product_db import Product_db

class Order_db:
    def __init__(self):
        self.db=db_session

    def close(self):
        self.db.close()

    def create_order(self, name, product, price, amount):
        result_creating_customer = Customer_db().create_customer(name)
        result_creating_product = Product_db().create_product(product)
        print(f"customer：{result_creating_customer} ； product：{result_creating_product}")
        customer_data = Customer_db().get_customer_data(name)
        product_data = Product_db().get_product(product)
        print(f"customer：{customer_data['customer_id']} ； product：{product_data['product_id']}")
        return "Order done"

    