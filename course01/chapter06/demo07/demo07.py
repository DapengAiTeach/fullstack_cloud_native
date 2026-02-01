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

# 新增电影数据
session = SessionLocal()
new_movie = Movie(
    title="功夫",
    director="陈凯歌",
    genre="动作",
    rating=8.8
)
session.add(new_movie)
session.commit()
session.close()
print("新增电影数据已提交成功。")

# 删除电影信息
session = SessionLocal()
movie_to_delete = session.query(Movie).filter(
    Movie.title == "功夫",
).first()
if movie_to_delete:
    session.delete(movie_to_delete)
    session.commit()
    print("电影信息已删除成功。")
else:
    print("未找到要删除的电影。")
session.close()

# 查询所有电影
session = SessionLocal()
movies = session.query(Movie).all()
for movie in movies:
    print(f"""电影ID: {movie.id}, 
          标题: {movie.title}, 
          导演: {movie.director}, 
          类型: {movie.genre}, 
          评分: {movie.rating}, 
          创建时间: {movie.created_at}""")
session.close()
print("所有电影数据已查询并显示成功。")