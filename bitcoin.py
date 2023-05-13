from fastapi import Depends
from sqlalchemy.orm import Session
import apikey
import requests
from Database import database_connection,model



header={
    'X-CMC_PRO_API_KEY' : apikey.key,
    'Accepts': "application/json"
}

params={
    'start':'1',
    'limit':'500',
    'convert':'USD'
}

url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

json= requests.get(url,params=params,headers=header).json()



