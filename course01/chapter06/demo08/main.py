from models.engine import Base, engine
from models.movie import Movie

# 初始化数据以后通过 Alembic 完成
print("数据库模型已导入，准备进行 Alembic 迁移操作。")