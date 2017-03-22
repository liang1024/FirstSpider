'''
主要内容:
1.函数作用域LEGB
2.闭包理解与使用
3.装饰器

1.LEGB：L>E>G>B
    L:local函数内部作用域
    E:enclosing 函数内部域内嵌函数之间
    G:global全局作用域
    B:build-in内置作用域

总结:函数作用域依次--> LEGB

2.闭包
    2-1:闭包概念
    Closure:内部函数中对enclosing作用域的变量进行引用

    函数实质域属性
    1.函数是一个对象
    2.函数执行完成后内部变量回收
    3.函数属性
    4.函数返回值

    2-2:闭包作用
    1.封装
    2.代码复用

3.python装饰器
    1.装饰器用来装饰函数
    2.返回一个函数对象
    3.被装饰函数标识符指向返回的函数对象
    4.语法糖 @deco


'''

# 闭包案例参考博客:
# http://www.cnblogs.com/ma6174/archive/2013/04/15/3022548.html

print('---------闭包案例1----------')


# 1.闭包案例1:
def make_adder(addend):
    def adder(augend):
        return augend + addend

    return adder


p = make_adder(23)
q = make_adder(44)
print(p(100))
print(q(100))
# 123
# 144

print('--------闭包案例2-----------')


# 闭包案例2:
def hellocounter(name):
    count = 0

    def counter():
        nonlocal count
        count += 1
        print('Hello,', name, ',', str(count) + ' access!')

    return counter


hello = hellocounter('liangzai')
hello()
hello()
hello()
# Hello, liangzai , 1 access!
# Hello, liangzai , 2 access!
# Hello, liangzai , 3 access!
print('--------闭包案例3-----------')


# 闭包案例3:
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


print(hello())
# <b><i>hello world</i></b>
