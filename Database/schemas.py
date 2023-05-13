from pydantic import BaseModel,EmailStr
import datetime


class Leads(BaseModel):
    name:str
    status:str
    account_name:str
    office_phone:str
    email:EmailStr
    users:str
    class Config:
        orm_mode: True

class BitCoin(BaseModel):
    bitcoins:str
    usd:int
    class Config:
        orm_mode: True