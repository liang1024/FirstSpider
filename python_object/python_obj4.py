# 目录:
# 1.类的多态:
# 多态要素:
#    1.继承
#    2.方法重写

# 2.python Magic Method:
#     体现:  __init__(self)    前后都有下划线
#  python类的实例化过程  __new__(self)  -->  __init__(self)   -->  __del__(self)

# 3.类与运算符:
# python自带的Magic method
#       3-1:比较运算符
#  __cmp__(self,other)    比较对象的大小
#  __eq__(self,other)     是否等于
#  __lt__(self,other)     是否小于
#  __gt__(self,other)     是否大于
#       3-2:数字运算符
#  __add__(self,other)     加
#  __sub__(self,other)     减
#  __mul__(self,other)     乘
#  __div__(self,other)     除
#       3-3:逻辑运算符
#  __or__(self,other)     或者
#  __and__(self,other)     和

class Programer:
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = int
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of Object must be Programer')

            # def __add__(self, other):
            #     if isinstance(other,Programer):
            #         return self.age+other.age
            #     else:
            #         raise Exception('The type of object must be Progeamer')


if __name__ == '__main__':
    p1 = Programer('Albert', 25)
    p2 = Programer('Bill', 30)
    print(p1 == p2)
    # print(p1+p2)



# 4.类的展现:
#       4-1.转换为字符串
#       __str__   不可作为代码运行
#       __repr__  可作为代码运行
#       __unicode__
#       4-2.展现对象属性
#       __dir__

# 5.类的属性访问
#       5-1.设置对象属性
#       __setattr_(self,name,value):
#
#       5-2.查询对象属性
#       __getattr__(self,name)
#       __getatribute__(self,name)
#       5-3.删除对象属性
#       __delattr__(self,name)

# 6.课程总结

#     6-1.面向对象理论
#     1.类和对象
#     2.属性和方法
#     3.继承

#     6-2.Python面向对象基础
#     1.定义类
#     2.定义属性和方法
#     3.继承

#     6-3.Magic Method
#     1.构造对象
#     2.运算符
#     3.类的展现
#     4.类的属性访问
#     5.更多Magic Method:python官网
