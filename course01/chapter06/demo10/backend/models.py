from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
)
from database import Base

class Movie(Base):
    """电影模型类，映射到数据库中的movies表"""
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    director = Column(String(100), nullable=False, index=True)
    genre = Column(String(50), nullable=False, index=True)
    rating = Column(Float, nullable=False)
    release_year = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
print("电影模型类已定义成功。")