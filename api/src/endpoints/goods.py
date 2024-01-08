from fastapi import APIRouter, HTTPException, Depends
from fastapi.params import Body
from typing import List
from api.src.utils.db import db_get_data
from api.src.utils.auth import get_current_user

router = APIRouter()

@router.get("/goods/{item_id}")
async def read_item(item_id: int, q: str = None, current_user: dict = Depends(get_current_user)):
    query = f"SELECT * FROM goods WHERE id = {item_id}"
    result = db_get_data(query)
    return {"item_id": item_id, "q": q, "data": result, "user": current_user}

@router.post("/goods")
async def create_item(item: dict = Body(...), current_user: dict = Depends(get_current_user)):
    query = f"INSERT INTO goods (name, price) VALUES ('{item['name']}', {item['price']})"
    result = db_get_data(query)
    return {"message": "Item created successfully", "user": current_user}
