import re

# 目录 sqlite
# 1.search 在一个字符串中查找匹配
# 2.findall找到匹配，返回索引匹配部分的列表
# 3.sub 将字符串中匹配正则表达式的部分替换为其他值
# 4.split 根据匹配分割字符串，返回字符串组成的列表


print('---------1.search  在一个字符串中查找匹配----------')
# 1.search  字符
str1 = 'imooc videonum = 1000'
print(str1.find('1000'))
# 2.使用search找到第一串数字
info = re.search(r'\d+', str1)
print(info.group())

print('---------2.findAll 找到匹配，返回索引匹配部分的列表----------')
# 1.使用search查询只能查询出第一个
str2 = 'c++=100, java=90, python=80'
info2 = re.search(r'\d+', str2)
print(info2.group())
# 2.使用findAll找到所有数字 并求和
info3 = re.findall(r'\d+', str2)
print(info3)
print(sum(int(x) for x in info3))  # 求和  for x in info3     int(x)    sum(x)

print('---------3.sub 将字符串中匹配正则表达式的部分替换为其他值----------')
# 1.将查找到的数字替换为1001
str3 = 'imooc videonum=1000'
info4 = re.sub(r'\d+', '1001', str3)
print(info4)

# 2.定义函数将每次遍历出来的数字进行 +1 (处理)
str4 = 'imooc videonum=9998'

def add(match):
    val = match.group()
    num = int(val) + 1
    return str(num)

info5 = re.sub(r'\d+', add, str4)
info6 = re.sub(r'\d+', add, info5)
print(info6)

print('---------4.split 根据匹配分割字符串，返回字符串组成的列表----------')
# 1.截取 :|空格|,|.    (注意：.需要进行转意 \.)
str5 = 'imooc:C C++ Java Python,C#.PHP'
_sqlit = re.split(r':| |,|\.', str5)
print(_sqlit)
#只截取两次
__sqlit = re.split(r':| |,|\.', str5,2)
print(__sqlit)
