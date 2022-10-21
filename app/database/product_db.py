from .db import db_session, Product

class Product_db:
    def __init__(self):
        self.db=db_session

    def close(self):
        self.db.close()

    def is_product_existed(self, product):
        if self.get_product(product):
            return True
        return False

    async def get_product(self, product):
        pd = self.db.query(Product).filter(Product.product_name == product).first()
        return pd

    async def create_product(self, product):
        if self.is_product_existed(product):
            return "Product existed"
        product=Product(product_name=product)
        db_session.add(product)
        db_session.commit()
        self.close()
        return "Product created"