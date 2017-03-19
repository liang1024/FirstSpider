import re

# 目录:
# 1.匹配前一个字符0次或无限次 *
# 2.匹配前一个字符1次或无限次 +
# 3.匹配前一个字符0次或1次 ?
# 4.匹配前一个字符m次或者m-n次 {m}/{m,n}
# 5.匹配模式变为非贪婪(尽可能少匹配) *？ /  +?  /?? 

print('-----------1.匹配前一个字符0次或无限次 * ---------------')
# 1.普通的匹配(有字数限制)
print(re.match(r'[A-Z][a-z]', 'Az').group())  # 只能匹配两个字符
# 2.限制第一个为大写,后面的匹配可以0-无限次
print(re.match(r'[A-z][a-z]*', 'A').group())
print(re.match(r'[A-z][a-z]*', 'Aasdsadasdsad').group())

print('-----------2.匹配前一个字符1次或无限次 + ---------------')
# 1.实例:python变量名 规则:首字母必须是 _ A-Z a-z  后面字符必须为[a-zA-Z0-9]
print(re.match(r'[_A-Za-z]+[_\w]*', '_asdsadsadsadas12321').group())

print('-----------3.匹配前一个字符0次或1次 ? ---------------')
# 1.匹配数字 0-99   bug:09会只显示0
print(re.match(r'[0-9]?[0-9]', '99').group())

print('-----------4.匹配前一个字符m次或者m-n次 {m}/{m,n} ---------------')
# 1.限制为{m}字
print(re.match(r'[A-Za-z0-9]{6}','123abc').group())
print(re.match(r'[A-Za-z0-9]{6}','123ab'))  #结果为：None
print(re.match(r'[A-Za-z0-9]{6}','123abcdef').group()) #只会保留6个
print(re.match(r'[\w]{6}@163.com','123456@163.com').group())  #限制为6位数的163邮箱
# 2.限制为{m,n}之间的数字
print(re.match(r'[\w]{6,10}@163.com','12345@163.com'))  #小于时为None
print(re.match(r'[\w]{6,10}@163.com','012356789@163.com').group()) #正常
print(re.match(r'[\w]{6,10}@163.com','0123567891abc@163.com')) #大于时为None

print('-----------5.匹配模式变为非贪婪(尽可能少匹配) *？ /  +?  /??  ---------------')
# 1.*?:匹配一般为0次
print(re.match(r'[A-Z][\w]*?','Aw12412hu13hrasf').group())  #[A-Z]为必须匹配  *？匹配为0次
# 1.+?:匹配一般为1次
print(re.match(r'[A-Z][\w]+?','Bw12412hu13hrasf').group())  #[A-Z]为必须匹配  *？匹配为1次
# 1.??:匹配一般为0次
print(re.match(r'[A-Z][\w]??','Cw12412hu13hrasf').group())  #[A-Z]为必须匹配  *？匹配为0次
