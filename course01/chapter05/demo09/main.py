from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    """商品模型"""
    id: int
    name: str
    price: float

# 模拟测试数据，用于接口练习
items = [
    {"id": 1, "name": "Apple", "price": 3.5},
    {"id": 2, "name": "Banana", "price": 2.0},
]

@app.get("/items/", response_model=list[Item])
async def read_items():
    """获取所有商品"""
    return items

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """创建新商品"""
    items.append(item.model_dump())
    return item