from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class MovieBase(BaseModel):
    """电影基础模型类，包含电影的基本信息"""
    title: str = Field(..., max_length=255, description="电影标题")
    director: str = Field(..., max_length=100, description="导演")
    genre: str = Field(..., max_length=50, description="类型")
    rating: float = Field(..., ge=0, le=10, description="评分，范围0-10")
    release_year: int = Field(..., ge=1888, le=datetime.now().year, description="上映年份")

class MovieCreate(MovieBase):
    """创建电影模型类，继承自MovieBase"""
    rating: Optional[float] = Field(None, ge=0, le=10, description="评分，范围0-10")
    release_year: Optional[int] = Field(None, ge=1888, le=datetime.now().year, description="上映年份")

class MovieUpdate(MovieBase):
    """更新电影模型类，所有字段均为可选"""
    title: Optional[str] = Field(None, max_length=255, description="电影标题")
    director: Optional[str] = Field(None, max_length=100, description="导演")
    genre: Optional[str] = Field(None, max_length=50, description="类型")
    rating: Optional[float] = Field(None, ge=0, le=10, description="评分，范围0-10")
    release_year: Optional[int] = Field(None, ge=1888, le=datetime.now().year, description="上映年份")

class MovieInDB(MovieBase):
    """数据库中的电影模型类，包含ID和创建时间"""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MovieResponse(MovieInDB):
    """响应模型类，继承自MovieInDB"""
    id: int
    created_at: datetime