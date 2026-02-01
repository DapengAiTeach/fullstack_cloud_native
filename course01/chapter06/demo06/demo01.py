import pymysql

# 连接到 MySQL 数据库
conn = pymysql.connect(
    host='localhost', # 主机地址
    port=13306, # 端口号
    user='movie_db', # 用户名
    password='movie_db', # 密码
    database='movie_db', # 数据库名称
    charset='utf8mb4', # 字符编码，支持中文
    cursorclass=pymysql.cursors.DictCursor, # 返回字典形式的结果
)
print("数据库连接成功！")

# 关闭连接
conn.close()
print("数据库连接已关闭！")