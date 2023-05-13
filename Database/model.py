from .database_connection import base
from sqlalchemy import Integer,String,Column,TIMESTAMP,Float

class Leads(base):
    __tablename__="leads"

    id=Column(Integer,autoincrement=True,primary_key=True,nullable=False)
    name=Column(String(255),nullable=False)
    status=Column(String(50),nullable=False)
    account_name=Column(String(50),nullable=False)
    office_phone=Column(String(20),nullable=False,unique=True) ##Since the phone number of 10 digits cant be stored in mysql in integer form so we store it as string
    email=Column(String(100),nullable=False,unique=True)
    users=Column(String(100),nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False)

class BitCoin(base):
    __tablename__="bitcoin"

    id=Column(Integer,autoincrement=True,nullable=False,primary_key=True)
    bitcoins=Column(String(255),nullable=False)
    usd=Column(Float)