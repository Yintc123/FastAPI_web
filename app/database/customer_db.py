from .db import db_session, Customer

# 操作資料庫 customer_table 的類別
class Customer_db:
    def __init__(self):
        self.db=db_session

    # 操作完成關閉連線，避免佔用資料庫資源
    def close(self):
        self.db.close()

    # 是否有顧客資訊
    def is_customer_existed(self, name):
        if self.get_customer_data(name):
            return True
        return False

    # 拿取顧客資料
    def get_customer_data(self, name):
        customer = self.db.query(Customer).filter(Customer.customer_name == name).first()
        return customer

    # 創建顧客資料
    async def create_customer(self, name):
        # 如果已有顧客資料
        if self.is_customer_existed(name):
            # 返回顧客已存在
            return "Customer existed"
        customer=Customer(customer_name=name)
        self.db.add(customer)
        self.db.commit()
        self.close()
        return "Customer created"