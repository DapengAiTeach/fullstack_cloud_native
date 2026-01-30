from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    """用户模型"""
    id: Optional[int] = Field(default=None, primary_key=True)
    # 用户名
    username: str = Field(min_length=2, max_length=36,index=True, unique=True)
    # 密码
    password: str = Field(min_length=6, max_length=128)
    is_active: bool = True