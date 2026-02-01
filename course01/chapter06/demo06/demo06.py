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

# 创建游标对象
with conn.cursor() as cursor:
    # 批量新增用户的SQL
    sql = "INSERT INTO users (username, age, city) VALUES (%s, %s, %s)"
    # 执行SQL语句
    users = [
        ("李四", 28, "广州"),
        ("王五", 32, "深圳"),
        ("赵六", 22, "杭州"),
        ("钱七", 27, "成都"),
        ("孙八", 29, "武汉"),
        ("周九", 31, "西安"),
    ]
    cursor.executemany(sql, users)
    # 提交事务
    conn.commit()
    print("用户批量添加成功！")

# 关闭连接
conn.close()
print("数据库连接已关闭！")