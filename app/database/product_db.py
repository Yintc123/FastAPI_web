from .db import db_session, Product

# 操作資料庫 product_table 的類別
class Product_db:
    def __init__(self):
        self.db=db_session

    # 操作完成關閉連線，避免佔用資料庫資源
    def close(self):
        self.db.close()

    # 是否有產品資訊
    def is_product_existed(self, product):
        if self.get_product(product):
            return True
        return False

    # 拿取產品資料
    def get_product(self, product):
        pd = self.db.query(Product).filter(Product.product_name == product).first()
        return pd

    # 創建產品資料
    async def create_product(self, product):
        # 如果已有產品資料
        if self.is_product_existed(product):
            # 返回產品已存在
            return "Product existed"
        product=Product(product_name=product)
        self.db.add(product)
        self.db.commit()
        self.close()
        return "Product created"