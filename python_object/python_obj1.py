
# 目录
# 1.类
# 2.类中属性的定义


print('--------1.类-----------')
class google:

    #1.构造函数
    def __init__(self):
        pass

    #2.类被回收时调用
    def __del__(self):
        pass

google=google()

# 1.type() 打印类的类型
print(type(google))
# 2.dir()打印类的属性
print(dir(google))

print('--------2.类中属性的定义-----------')

class Programer:
    #1.直接在类中定义
    sex='male'

    def __init__(self):
        self.name='lz'
        self.age='20'


if __name__=='__main__':
    programer=Programer()
    print(programer.__dict__) #2.从构造函数中获得的属性