from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

class Item(BaseModel):
    """商品模型"""
    id: int
    name: str
    price: float

# 模拟测试数据，用于接口练习
items = [
    {"id": 1, "name": "苹果", "price": 3.5},
    {"id": 2, "name": "香蕉", "price": 2.0},
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