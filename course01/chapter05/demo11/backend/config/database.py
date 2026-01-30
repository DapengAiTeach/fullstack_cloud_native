from sqlmodel import SQLModel, create_engine

# 数据库连接配置
DATABASE_URL = "sqlite:///./test.db"
# 创建数据库引擎
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """初始化数据库"""
    SQLModel.metadata.create_all(engine)