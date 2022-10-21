import asyncio
from .db import Customer, Product, db_session, Order
from .customer_db import Customer_db
from .product_db import Product_db

# 操作資料庫 order_table 的類別
class Order_db:
    def __init__(self):
        self.db=db_session

    # 操作完成關閉連線，避免佔用資料庫資源
    def close(self):
        self.db.close()

    # 拿取單個訂單資料
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

    # 拿取所有訂單資料
    async def get_orders(self):
        orders = self.db.query(Order.order_id, Customer.customer_name,
                                Product.product_name, Order.amount, 
                                Order.price, (Order.amount*Order.price).label('total'))\
                        .join(Customer).join(Product)\
                        .filter(Order.customer_id==Customer.customer_id)\
                        .filter(Order.product_id==Product.product_id).all()
        self.close()
        return orders

    # 建立訂單資料
    async def create_order(self, name, product, price, amount):
        # 如果無顧客及產品資訊，建立顧客及產品資訊，建立需一定時間，所以使用非同步方法，使其幾乎同時執行建立顧客及產品資料
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

    # 修改訂單資料
    async def modify_order(self, name, product, price, amount, order_id):
        # 如果無顧客及產品資訊，建立顧客及產品資訊，建立需一定時間，所以使用非同步方法，使其幾乎同時執行建立顧客及產品資料
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

    