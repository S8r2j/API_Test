from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

db_url="mysql+pymysql\://root:password@localhost:3306/test"

engine=create_engine(db_url)
session=sessionmaker(autoflush=False,bind=engine)
base=declarative_base()

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()