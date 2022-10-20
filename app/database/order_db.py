from .db import db_session, Order
from .customer_db import Customer_db
from .product_db import Product_db

class Order_db:
    def __init__(self):
        self.db=db_session

    def close(self):
        self.db.close()

    def create_order(self, name, product, price, amount):
        pass

    