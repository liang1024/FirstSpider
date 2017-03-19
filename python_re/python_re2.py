import re

#目录
# 1:匹配任意字符 .
# 2:匹配字符集 [...]
# 3:匹配数字/非数字 \d /\D
# 4:匹配单词字符[a-zA-Z0-9]/非单词字符  \w / \W



print('-------1.匹配任意字符 . -------')
# 1.匹配任意字符
print(   re.match(r'.','1',) .group()  )
# 2.匹配大括号{} 中的任意字符
print(re.match(r'{.}','{6}').group())

print('-------2.匹配字符集 [...] -------')
# 1.[abc]:匹配abc
print(re.match(r'[abc]','a').group())
# 2.[a-z]:匹配a-z
print(re.match(r'[a-z]','z').group())
# 3.[A-Z]:匹配A-Z  大写
print(re.match(r'[A-Z]','Z').group())
# 4.[0-9]:匹配0-9
print(re.match(r'[0-9]','8').group())
# 4.[a-zA-Z0-9]:匹配a-zA-Z0-9
print(re.match(r'[a-zA-Z0-9]','G').group())

print('-------3.匹配数字/非数字 \d /\D -------')
# 1.匹配数字：\d
print(re.match(r'\d','2').group())
print(re.match(r'\d','d'))  #结果为：None
# 2.匹配非数字： /\d
print(re.match(r'\D','d').group())
print(re.match(r'\D','2'))  #结果为：None

print('-------4.匹配单词字符[a-zA-Z0-9]/非单词字符  \w / \W-------')
# 1.匹配单词字符\w
print(re.match(r'\w','A').group())
print(re.match(r'\w','AA').group())
# 2.匹配非单词字符\W
print(re.match(r'\W','-').group())
print(re.match(r'\W','&').group())
print(re.match(r'\W',' ').group())  #空格
# 3.匹配字符集中的字符 使用 \w
#   3-1:匹配字符集
print(re.match(r'[\w]','Z').group())
#   3-2:匹配 中括号中的字符:  [[\w]]
print(re.match(r'\[[\w]\]','[Z]').group())

