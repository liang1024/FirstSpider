# Python定义方法：
# 1.方法可以赋值为字符串,python中类的方法也可以看成类的属性
# 2.拿到类的实例化然后调用方法
# 3.通过累类名调用方法
# 4.通过类名像调用属性一样调用方法
class Test:
    def test(self):
        pass

a = Test()
print(a.test)
# <bound method Test.test of <python_object.python_obj2.Test object at 0x02E46E90>>

#  1.方法可以赋值为字符串
a.test = "1234"
print(a.test)
# 1234
print('--------------------------------')

# @classmethod   调用的时候用类名，而不是某个对象
# @property 像访问属性一样访问方法

class Programer:
    def get_name(self):
        print('获取名字')

    @classmethod
    def get_hobby(self):
        print("获取hobby")

    @property
    def get_weight(self):
        print('获取weight')


programer = Programer()

print(programer.get_weight)  #2.拿到类的实例化然后调用方法
print(Programer.get_hobby()) #3.通过累类名调用方法
print(Programer.get_weight)  #4.通过类名像调用属性一样调用方法
