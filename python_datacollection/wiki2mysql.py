# 引入开发包
from urllib.request import urlopen  # 请求网页
from bs4 import BeautifulSoup  # 解析网页
import re  # 正则匹配
import pymysql.cursors

url = "https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"
resp = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(resp, "html.parser")
listurls = soup.find_all("a", href=re.compile("^/wiki/"))

for url in listurls:
    if not re.search("\.(jpg|JPG)$", url["href"]):
        print(url.get_text() + "------" + "https://zh.wikipedia.org" + url["href"])
        # 连接数据库
        connection = pymysql.connect(host="localhost",
                                     user="root",
                                     password="971019",
                                     db="wikiurl",
                                     charset="utf8mb4")
        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建sql语句
                sql = "insert into `urls`(`urlname`,`urlhref`) values(%s,%s)"
                # 执行sql
                cursor.execute(sql, (url.get_text(), "https://zh.wikipedia.org" + url["href"]))
                # 提交
                connection.commit()
        finally:
            # 确保关闭资源
            connection.close()
