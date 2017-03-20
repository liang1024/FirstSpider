
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
    def __init__(self,name,age):
        self.name=name
        if isinstance(age,int):
            self.age=int
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other,Programer):
            if self.age==other.age:
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


if __name__=='__main__':
    p1=Programer('Albert',25)
    p2=Programer('Bill',30)
    print(p1==p2)
    # print(p1+p2)