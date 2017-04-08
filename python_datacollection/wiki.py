# 引入开发包
from urllib.request import urlopen #请求网页
from bs4 import BeautifulSoup #解析网页
import re #正则匹配

url="https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"

resp=urlopen(url).read().decode("utf-8")

soup=BeautifulSoup(resp,"html.parser")
listurls=soup.find_all("a",href=re.compile("^/wiki/"))

for url in listurls:
    # if not re.search("\.(jpg|JPG)$",url["href"]):
        print(url.get_text()+"------"+"https://zh.wikipedia.org"+url["href"])







