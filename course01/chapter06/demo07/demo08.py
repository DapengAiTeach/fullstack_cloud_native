from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
)
from sqlalchemy.orm import sessionmaker, declarative_base

# 数据库连接字符串
DATABASE_URL = "mysql+pymysql://movie_db:movie_db" \
"@localhost:13306/movie_db"

# 创建数据库引擎
engine = create_engine(
    DATABASE_URL, 
    echo=True, # 显示SQL语句日志
    pool_size=10, # 连接池大小
    max_overflow=20, # 连接池最大溢出数
    future=True, # 启用SQLAlchemy 2.0风格
)

# 创建会话工厂
SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, # 关闭自动刷新
    autocommit=False, # 关闭自动提交
    future=True, # 启用SQLAlchemy 2.0风格
)

# 创建声明基类
Base = declarative_base()

print("数据库引擎和会话工厂已创建成功。")

class Movie(Base):
    """电影模型类，映射到数据库中的movies表"""
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    director = Column(String(100), nullable=False, index=True)
    genre = Column(String(50), nullable=False, index=True)
    rating = Column(Float, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
print("电影模型类已定义成功。")

# 初始化数据库表
Base.metadata.drop_all(bind=engine)  # 如果表已存在则删除
Base.metadata.create_all(bind=engine) # 创建所有表
print("数据库表已创建成功。")

# 批量新增电影数据
session = SessionLocal()
movies_data = [
    {
        "title": "功夫",
        "director": "陈凯歌",
        "genre": "动作",
        "rating": 8.8
    },
    {
        "title": "卧虎藏龙",
        "director": "李安",
        "genre": "武侠",
        "rating": 9.2
    },
    {
        "title": "英雄",
        "director": "张艺谋",
        "genre": "历史",
        "rating": 8.5
    }
]
for movie_data in movies_data:
    movie = Movie(**movie_data)
    session.add(movie)
session.commit()
session.close()
print("批量新增电影数据已提交成功。")

# 根据电影名或者导演名模糊搜索：功夫
session = SessionLocal()
search_keyword = "功夫"
movies = session.query(Movie).filter(
    (Movie.title.like(f"%{search_keyword}%")) |
    (Movie.director.like(f"%{search_keyword}%"))
).all()
for movie in movies:
    print(f"""
          电影ID: {movie.id}, 
          标题: {movie.title}, 
          导演: {movie.director}, 
          类型: {movie.genre}, 
          评分: {movie.rating}, 
          创建时间: {movie.created_at}""")