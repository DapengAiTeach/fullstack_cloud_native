from models.engine import Base, engine
from models.movie import Movie

# 初始化数据库表
Base.metadata.drop_all(bind=engine)  # 如果表已存在则删除
Base.metadata.create_all(bind=engine) # 创建所有表
print("数据库表已创建成功。")