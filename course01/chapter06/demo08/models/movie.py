from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
)
from models.engine import Base

class Movie(Base):
    """电影模型类，映射到数据库中的movies表"""
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    director = Column(String(100), nullable=False, index=True)
    genre = Column(String(50), nullable=False, index=True)
    rating = Column(Float, nullable=False, index=True)
    release_year = Column(Integer)  # 新增上映年份
    created_at = Column(DateTime, default=datetime.utcnow)
print("电影模型类已定义成功。")