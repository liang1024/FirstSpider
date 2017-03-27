from urllib import request
from urllib.request import Request
from urllib.request import urlopen
from urllib import parse

from bs4 import BeautifulSoup

'''获取百度的源码'''
print("----------添加Header之前-------------")
resp = request.urlopen("http://www.baidu.com")
# print(resp.read().decode("utf-8"))

print("----------添加Header之后-------------")

req2 = request.Request("http://www.baidu.com")
req2.add_header("User-Agent",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
resp2 = request.urlopen(req2)
# print(resp2.read().decode('utf-8'))


print("----------POST方法-------------")

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
# body post内容
postdata = parse.urlencode(
    [("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"), ("EndStation", "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
     ("SearchDate", "2017/03/28"), ("SearchTime", "08:00"), ("SearchWay", "DepartureInMandarin")])
# 添加head
req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3")
# 
resp = urlopen(req, data=postdata.encode("utf-8"))

print(resp.read().decode("utf-8"))
