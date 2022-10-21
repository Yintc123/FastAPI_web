import asyncio
from .db import db_session, Customer

class Customer_db:
    def __init__(self):
        self.db=db_session

    def close(self):
        self.db.close()

    def is_customer_existed(self, name):
        if self.get_customer_data(name):
            return True
        return False

    def get_customer_data(self, name):
        print("****get customer start")
        customer = self.db.query(Customer).filter(Customer.customer_name == name).first()
        print("****get customer end")
        return customer

    async def create_customer(self, name):
        print("****create customer start")
        if self.is_customer_existed(name):
            return "Customer existed"
        customer=Customer(customer_name=name)
        db_session.add(customer)
        db_session.commit()
        self.close()
        print("****create customer end")
        return "Customer created"