from fastapi import FastAPI,HTTPException,Request
from pydantic import BaseModel,HttpUrl
from datetime import datetime,timedelta

from typing import Dict
app=FastAPI()
url_store:Dict[str,dict]={}
class ShortURL(BaseModel):
    long_url:HttpUrl
    validity:int
    shortcode:str
@app.post("/shorten")
def shorten_url(req:ShortURL,request:Request):
    if req.shortcode in url_store:
        return {"error":"Shortcode already exists"}
    expiration_time=datetime.now()+timedelta(seconds=req.validity)
    url_store[req.shortcode]={"long_url":req.long_url,"expires_at":expiration_time}
    host=request.base_url._url.rstrip("/")
    return {"shortlink":f"{host}/{req.shortcode}",
            "expiry":expiration_time}
@app.get("/{shortcode}")
def redirect(shortcode:str):
    entry=url_store.get(shortcode)
    if not entry or entry["expires_at"]<datetime.now().timestamp():
        raise HTTPException(status_code=404,detail="Shortcode not found or expired")
    return {"long_url":entry["long_url"]}
