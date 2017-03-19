import re

# 目录
# 1.匹配字符串开头
# 2.匹配字符串结尾
# 3.^ 与$ 一起使用
# 4.指定的字符串必须在开头/结尾  \A / \Z
# 5.匹配左右任意一个表达式  |
# 6.括号中表达式作为一个分组  （ab）
# 7.引用编号为num的分组匹配到的字符串  \<number>
# 8.分组起一个别名  （?P<name>）
# 9.引用别名为name的分组匹配字符串  （?P=name）

print('-----------1.匹配字符串开头  ^ --------------')
# 1. 匹配字符串开头
print(re.match(r'^[0-9]+', '0123456789').group())
print(re.match(r'^[0-9]+', 'A0123456789'))  # None

print('-----------2.匹配字符串结尾  $ --------------')
# 1.匹配字符串结尾
print(re.match(r'[0-9]+', '0123456789').group())
print(re.match(r'[0-9]+$', 'A0123456789A'))  # None

print('-----------3.^ 与$ 一起使用--------------')
# 1.开头必须4-10位 结尾必须@163.com
print(re.match(r'^[\w]{4,10}@163.com$', 'A0123456789A'))  # None
print(re.match(r'^[\w]{4,10}@163.com$', '1234@163.com').group())  # 正确的163邮箱

print('-----------4.指定的字符串必须在开头/结尾  \A / \Z --------------')
# 1.指定字符串必须在开头  \A
print(re.match(r'\A[0-9][\w]*', '1saxasucbhsa12r1efcAcdAAA').group())
print(re.match(r'\A[0-9][\w]*', 'Asaxasucbhsa12r1efcAcdAAA'))  # None
# 2.指定字符串必须在结尾  \Z
print(re.match(r'[\w]*[0-9]\Z', 'Asaxasucbhsa12r1efcAcdAAA'))  # None
print(re.match(r'[\w]*[0-9]\Z', '1saxasucbhsa12r1efcAcdAAA0').group())
# 3.指定开头和结尾必须为0-9
print(re.match(r'\A[0-9][\w]+[0-9]\Z', 'asasd12'))  # None
print(re.match(r'\A[0-9][\w]+[0-9]\Z', '11asas'))  # None
print(re.match(r'\A[0-9][\w]+[0-9]\Z', '1asas1').group())

print('-----------5.匹配左右任意一个表达式  | --------------')
# 1. 只要左右有一个匹配就算通过
print(re.match(r'abc|d', 'abc').group())
print(re.match(r'abc|d', 'd').group())
# 2.匹配数字0-99之间
print(re.match(r'[1-9]?\d$', '9').group())
print(re.match(r'[1-9]?\d$', '99').group())
print(re.match(r'[1-9]?\d$', '90').group())
print(re.match(r'[1-9]?\d$', '09'))  # None
# 3.匹配数字0-99或者100
print(re.match(r'[1-9]?\d$|100', '99').group())
print(re.match(r'[1-9]?\d$|100', '100').group())

print('-----------6.括号中表达式作为一个分组  （ab） --------------')
# 1.分组:()邮箱匹配
print(re.match(r'[\w]{4,10}@(163|126|qq|gmail).com', '123456@163.com').group())
print(re.match(r'[\w]{4,10}@(163|126|qq|gmail).com', '123456@126.com').group())
print(re.match(r'[\w]{4,10}@(163|126|qq|gmail).com', '123456@qq.com').group())
print(re.match(r'[\w]{4,10}@(163|126|qq|gmail).com', '123456@gmail.com').group())
print(re.match(r'[\w]{4,10}@(163|126|qq|gmail).com', '123456@yahoo.com'))  # None 只能匹配()分组中的值

print('-----------7.引用编号为num的分组匹配到的字符串  \<number>--------------')
# 1.引用编号为num的分组匹配到的字符串
print(re.match(r'<[\w]+>', '<book>').group())
print(re.match(r'<([\w]+>)[\w]+</\1', '<book>Python</book>').group())

print('-----------8.分组起一个别名  （?P<name>）--------------')
# 1.分组起一个别名  ?P<mark>
print(re.match(r'<(?P<mark>[\w]+>)[\w]+</\1', '<book>Python</book>').group())

print('-----------9.引用别名为name的分组匹配字符串  （?P=name）--------------')
# (?P=mark)
print(re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>Python</book>').group())
