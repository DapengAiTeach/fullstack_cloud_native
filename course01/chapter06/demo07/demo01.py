from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 数据库连接字符串
DATABASE_URL = "mysql+pymysql://movie_db:movie_db" \
"@localhost:3306/movie_db"

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