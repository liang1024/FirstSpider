import re

# 目录：
# 1.字符串的匹配
# 2.正则的匹配
# 3.匹配下划线
# 4.大小写匹配
# 5.返回tuple
# 6.直接使用match方法


str = 'imooc python'
print('----------1.字符串的匹配--------------')
# 字符串的匹配
print(str.find('11'))  # 没有值时会返回-1
print(str.find('imooc'))  # 返回起点索引下标:
print(str.startswith('imooc'))  # 返回是否在列表中  True 或False

print('----------2.正则的匹配--------------')

# 正则的匹配  r :匹配输入的原字符串(例如:\n换行 也会是字符串的\n)
# pa=re.compile(r'imooc\n')
pa = re.compile(r'imooc')

# 打印pa的类型
print(type(pa))  # <class '_sre.SRE_Pattern'>

ma = pa.match(str)
print(ma)  # 匹配     匹配失败为None 成功则为对象:<_sre.SRE_Match object; span=(0, 5), match='imooc'>

# print(help(ma))  help()  方法可以打印出变量所拥有的方法

str = ma.group()  # 拿到匹配的字符串或tuple
print(str)

span = ma.span()  # 拿到元素所在的索引位置
print(span)

string = ma.string  # 拿到被匹配的字符串  imooc python
print(string)

re_ = ma.re  # 被匹配的实例被放在 re 方法中
print(re_)

print('-------3.匹配下划线----------')

# 例子1:  匹配下划线
_value = '_value'

_pa = re.compile(r'_')

_ma = _pa.match(_value)

_group = _ma.group()

print(_group)

print('-------4.大小写匹配----------')
# 例子2:大小写匹配  参数2:re.I 忽略大小写

# 正常匹配
_pa=re.compile(r'imooc', re.I)
ma=_pa.match('imooc python')
_group=ma.group()
print(_group)

# I O 大写
__pa=re.compile(r'imooc', re.I)
__ma=__pa.match('ImoOc python')
__group=__ma.group()
print(__group)

print('-------5.返回tuple----------')

___pa=re.compile(r'(imooc)',re.I)
___ma=___pa.match('imooc python')

print(___ma.group()) #返回匹配字符串
print(___ma.groups()) #返回元祖形式


print('-------6.直接使用match方法----------')

____ma=re.match(r'imooc',str)
print(___ma.group())
print(___ma.groups())