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
url_mysql=f"mysql+pymysql://{os.getenv('Database_root_'+env)}:{os.getenv('Database_password_'+env)}@localhost:3306/test"
engine = create_engine(url_mysql, echo=True)

# 創建 ORM 模型
Base = declarative_base()

# 創建 ORM 物件
class Order(Base):
    __tablename__ = "order_table"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(40), nullable=False)
    customer_id = Column(Integer, nullable=False)
    purchase_time = Column(DateTime, default=datetime.datetime.utcnow)

# 於資料庫創建與 Order 對應的 Table
# 至 engine 資料庫中創建所有繼承 Base 類別的 ORM 物件
Base.metadata.create_all(engine)

# sqlalchemy
session = sessionmaker(engine)
db_session=session()