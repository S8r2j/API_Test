from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from Database import model, database_connection,schemas
import datetime
from bitcoin import json

router=APIRouter()

model.base.metadata.create_all(bind=database_connection.engine)
@router.post("/data")
async def create_user(user:schemas.Leads,db:Session=Depends(database_connection.get_db)):
    user_details= model.Leads(name=user.name,status=user.status,account_name=user.account_name,office_phone=user.office_phone,email=user.email,users=user.users,created_at=datetime.datetime.utcnow())
    db.add(user_details)
    db.commit()
    db.refresh(user_details)
    return user_details

@router.get("/data")
async def get_userData(db:Session=Depends(database_connection.get_db)):
    user_details=db.query(model.Leads).all()
    return user_details



@router.post("/cryptoprice")
async def get_bitcoin_price(db:Session=Depends(database_connection.get_db)):
    coins = json['data']
    for x in coins:
        bit=model.BitCoin(bitcoins=x['symbol'], usd=x['quote']['USD']['price'])
        db.add(bit)
        db.commit()
        db.refresh(bit)
    return {"message":"updated successfully"}

@router.get("/cryptoprice")
async def get_bitcoin_price(db:Session=Depends(database_connection.get_db)):
    details=db.query(model.BitCoin).all()
    return details