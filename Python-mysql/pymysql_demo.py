import pymysql
'''
建库选择 utf8mb4编码

建表语句：
CREATE TABLE `person` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


'''

def insert_mysql():
    '''
    插入
    :return:
    '''
    connection = pymysql.connect(host="localhost", #数据库地址，本地为：localhost
                                 user="root",   #登录名
                                 password="lz971019.",  #数据库密码
                                 db="test",    #数据库名
                                 charset="utf8mb4")  #编码格式
    try:
        # 获取会话指针
        with connection.cursor() as cursor:
            for i in range(1000):
                print("插入数据成功:" + str(i))
                # 创建sql语句
                sql = "insert into `person`(`name`,`age`) values(%s,%s)"
                # 执行sql
                cursor.execute(sql, ("name"+ str(i), i))
                # 提交
                connection.commit()
    finally:
        # 确保关闭资源
        connection.close()


def query_mysql():
    '''
    查询
    :return:
    '''
    connection = pymysql.connect(host="localhost",  # 数据库地址，本地为：localhost
                                 user="root",  # 登录名
                                 password="lz971019.",  # 数据库密码
                                 db="test",  # 数据库名
                                 charset="utf8mb4")  # 编码格式
    try:
        # 获取会话指针
        with connection.cursor() as cursor:

            # 查询语句(查询条件)
            # sql="select * from person"   #查询person表中所有数据
            # sql = "select `name` from `person`"   #查询name 来自 person表
            # sql = "select `name`,`age` from `person` where `id` is not null"   #查询name age 来自person表  并且 id不为null
            # sql = "select `name`,`age` from `person` where `id` is null"   #查询name age 来自person表  并且 id为null
            # sql="select * from person where id<=5;"   #查询 id小于等于5
            # sql="select * from person where name='name100'; "   #查询name等于100
            # sql="select * from person where id<=30 and age=>10;"   #id小于等于30 ，age大于等10

            # 模糊查询
            # sql="select * from person where name like '%00';"   #查询尾数是00的数字
            # sql="select * from person where name like '%00' or name like 'name99%'; "   #查询尾数是00的数字，或者是name99开头的数字
            # sql="select * from person where name like 'name_';"   #name后面尾数是1位的数字

            # 固定查询
            # sql="select * from person where id in(1,3,8,10,11,100); "   #查询id为：1,3,8,10,11,100的数字

            # 范围
            # sql="select * from person where id between 3 and 8;"   #查询id为3-8的数字

            # 分页   select * from 表名 limit start,count 从start开始，获取count条数据
            sql="select * from person limit 100,20 "   #从10开始，获取20条数据， 不包含第100条

            # 总条数
            count = cursor.execute(sql)
            print("总条数:"+str(count))

            # 查询出1条数据
            result1 = cursor.fetchone()
            print("查询出1条数据:")
            print(result1)

            # 查询出3条数据
            result2 = cursor.fetchmany(size=2)
            print("查询出3条数据:")
            print(result2)

            # 查询出所有数据
            print("查询出所有数据:")
            resultall=cursor.fetchall()
            print(resultall)


    finally:
        # 确保关闭资源
        connection.close()


def delete_mysql():
    '''
    删除
    :return:
    '''
    connection = pymysql.connect(host="localhost",  # 数据库地址，本地为：localhost
                                 user="root",  # 登录名
                                 password="lz971019.",  # 数据库密码
                                 db="test",  # 数据库名
                                 charset="utf8mb4")  # 编码格式
    try:
        # 获取会话指针
        with connection.cursor() as cursor:

            #其他语句参考查询方法
            # sql = "DELETE FROM `person` WHERE id=2"       #删除id为2的数字
            # sql = "DELETE FROM `person` WHERE id in(3,5)"  #删除id为3 和5的数字
            sql = "DELETE FROM `person` WHERE id  between 6 and 8;"  #删除id为6-8的数字

            # 执行sql
            result=cursor.execute(sql)
            if result>0:
                print("删除成功，影响的行数："+str(result))
            else:
                print("删除失败，影响的行数："+str(result))
            # 提交
            connection.commit()
    finally:
        # 确保关闭资源
        connection.close()


def update_mysql():
    '''
    更新
    :return:
    '''
    connection = pymysql.connect(host="localhost",  # 数据库地址，本地为：localhost
                                 user="root",  # 登录名
                                 password="lz971019.",  # 数据库密码
                                 db="test",  # 数据库名
                                 charset="utf8mb4")  # 编码格式
    try:
        # 获取会话指针
        with connection.cursor() as cursor:

            # 其他语句参考查询方法
            # UPDATE 表名 SET 字段名=字段值 WHERE 条件
            sql = "UPDATE `person` SET name='张三' WHERE id=20;"  #修改id为20的name字段为张三

            # 执行sql
            result = cursor.execute(sql)
            if result > 0:
                print("修改成功，影响的行数：" + str(result))
            else:
                print("修改成功，影响的行数：" + str(result))
            # 提交
            connection.commit()
    finally:
        # 确保关闭资源
        connection.close()

if __name__ == '__main__':
    # insert_mysql()   #插入mysql表
    # query_mysql()     #查询
    # delete_mysql()    #删除
    # update_mysql()    #更新
    pass