import datetime
import os
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv, find_dotenv

# 使用 .env 檔的資料
load_dotenv(find_dotenv())
env=os.getenv('MODE')

# 創建 db 連接
url_mysql=f"mysql+pymysql://{os.getenv('Database_root_'+env)}:{os.getenv('Database_password_'+env)}@{os.getenv('Database_host_'+env)}:{os.getenv('Database_port_'+env)}/test"
# echo = True：將所有執行的過程輸出到 cmd or terminal
# pool_pre_ping = True：每次從 Connection Pool 取得連線時，就試著執行一次相當於 SELECT 1 的 SQL ，如果有問題，就可以重新建立新的連線取代失效的連線
# pool_recycle = 3600：連線池時間上限，設定連線時間超過 1 小時候斷線；由於每小時會做斷線的動作，所以會與 MySQL 通訊，使 MySQL 不會閒置 8 小時
# pool_size = 20：設定連線池大小，設定為 20 條連線
# max_overflow=0：連線能超出連線池的數量，設定為 0 ，不得超出連線池的數量
engine = create_engine(url_mysql, echo=True, pool_pre_ping=True, pool_recycle=3600, pool_size=20, max_overflow=0)

# 創建 ORM 模型
Base = declarative_base()

# 創建 ORM 物件
class Customer(Base):
    __tablename__ = "customer_table"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(40), nullable=False)
    create_time = Column(DateTime, default=datetime.datetime.utcnow)

# 創建 ORM 物件
class Product(Base):
    __tablename__ = "product_table"
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(40), nullable=False, unique=True)
    create_time = Column(DateTime, default=datetime.datetime.utcnow)

# 創建 ORM 物件
class Order(Base):
    __tablename__ = "order_table"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer_table.customer_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('product_table.product_id', ondelete='CASCADE'), nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    purchase_time = Column(DateTime, default=datetime.datetime.utcnow)

# 於資料庫創建與 Order 對應的 Table
# 至 engine 資料庫中創建所有繼承 Base 類別的 ORM 物件
Base.metadata.create_all(engine)

# sqlalchemy
session = sessionmaker(engine)
db_session=session()