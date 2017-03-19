import urllib.request
import re
import os

# 目录:
# Python正则表达式练习:
# 抓取网页中的图片保存到本地
# 1.抓取网页
# 2.获取图片地址
# 3.抓取网页内容并保存到本地

url = "http://www.imooc.com/course/list"
flie = 're6_imgs'
i = 0
html=urllib.request.urlopen(url).read().decode('utf-8')
urllist = re.findall(r'http://.+\.jpg',html)

if os.path.exists(flie): #判断文件夹是否已经存在
    print("文件夹已经存在了。")
else:
    os.makedirs(flie) #创建文件夹

for url in urllist:
    filename=flie + '/' + str(i) + '.jpg'
    urllib.request.urlretrieve(url,filename) #保存图片的代码
    print('保持文件'+filename+' 成功')
    i += 1
