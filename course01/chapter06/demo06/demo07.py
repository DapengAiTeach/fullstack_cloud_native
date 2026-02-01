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
    # 分页查询数据
    # 根据 id 降序排列，分页查询用户数据
    sql = "SELECT * FROM users ORDER BY id DESC LIMIT %s OFFSET %s"
    
    # 设置分页参数
    page = 1 # 页码
    page_size = 2 # 每页条数
    
    # 计算偏移量
    limit = page_size
    offset = (page - 1) * page_size

    # 执行SQL语句
    cursor.execute(sql, (limit, offset))
    results = cursor.fetchall()
    for row in results:
        print(row)
    print("分页查询成功！")

# 关闭连接
conn.close()
print("数据库连接已关闭！")