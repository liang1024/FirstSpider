
# 目录
# 类的继承
# Object是所有类的父类
# 1.Tony继承于Person类(继承的声明)
# 2.调用父类方法
# 3.子类的类型判断
# 4.python支持多继承

print('-------1.Tony继承于Person类----------')
# 1.Python中的继承声明是在类名的()中声明自己的父类
# 如下:Tony继承于Person类
class Person():
    pass
class Tony(Person):
    pass

print('-------2.调用父类方法----------')
# 2.调用父类方法:
class A:
    def AMethod(self):
        print('我是父类的方法')

class B(A):
    def BMethod(self):
        print('我是子类的方法')

b=B()
print(b.BMethod())
print(b.AMethod())

print('-------3.子类的类型判断----------')

# 3.子类的类型判断
#   3-1:isInstance  是否是实例化类型
#   3-2:issubclass  是否是子类

print(isinstance(b,B))
print(issubclass(B,A))

print('------------4.python支持多继承--------------------')
# 4.python支持多继承
# class Tony(Person,Man,brilliant):
