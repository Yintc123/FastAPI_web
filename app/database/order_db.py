import asyncio
from .db import Customer, Product, db_session, Order
from .customer_db import Customer_db
from .product_db import Product_db

class Order_db:
    def __init__(self):
        self.db=db_session

    def close(self):
        self.db.close()

    async def get_order(self, order_id):
        order = self.db.query(Customer.customer_name, 
                                Product.product_name,
                                Order.amount,
                                Order.price            
                            )\
                            .join(Customer).join(Product)\
                            .filter(Order.customer_id==Customer.customer_id)\
                            .filter(Order.product_id==Product.product_id)\
                            .filter(Order.order_id==order_id).first()

        self.close()
        return order

    async def get_orders(self):
        orders = self.db.query(Order.order_id, Customer.customer_name,
                                Product.product_name, Order.amount, 
                                Order.price, (Order.amount*Order.price).label('total'))\
                        .join(Customer).join(Product)\
                        .filter(Order.customer_id==Customer.customer_id)\
                        .filter(Order.product_id==Product.product_id).all()
        self.close()
        return orders

    async def create_order(self, name, product, price, amount):
        result_creating_customer = await asyncio.create_task(Customer_db().create_customer(name))
        result_creating_product = await asyncio.create_task(Product_db().create_product(product))
        customer_data = Customer_db().get_customer_data(name)
        product_data = Product_db().get_product(product)

        order = Order(customer_id = customer_data.customer_id, 
                        product_id = product_data.product_id, 
                        amount = amount, 
                        price = price)
        self.db.add(order)
        self.db.commit()
        self.close()

        return "Order done"

    async def modify_order(self, name, product, price, amount, order_id):
        result_creating_customer = await asyncio.create_task(Customer_db().create_customer(name))
        result_creating_product = await asyncio.create_task(Product_db().create_product(product))
        customer_data = Customer_db().get_customer_data(name)
        product_data = Product_db().get_product(product)

        order_info = {
            "customer_id":customer_data.customer_id,
            "product_id":product_data.product_id,
            "amount":amount,
            "price":price
        }

        order = db_session.query(Order).filter(Order.order_id==order_id)\
                            .update(order_info)
        self.db.commit()
        self.close()

        return "order modified done"

    