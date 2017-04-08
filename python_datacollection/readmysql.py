import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host="localhost",
                             user="root",
                             password="971019",
                             db="wikiurl",
                             charset="utf8mb4")
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 查询语句
        sql = "select `urlname`,`urlhref` from `urls` where `id` is not null"

        # 总条数
        count = cursor.execute(sql)
        print(count)
        # 234

        # 查询出所有数据
        # resultall=cursor.fetchall()
        # print(resultall)
        # 查询出3条数据
        result3 = cursor.fetchmany(size=3)
        print(result3)

finally:
    # 确保关闭资源
    connection.close()
