# Python:


## Python之print语句

print语句可以向屏幕上输出指定的文字。比如输出'hello, world'，用代码实现如下：
    
    >>> print 'hello, world'
    
注意：1.当我们在Python交互式环境下编写代码时，`>>>`是Python解释器的提示符，不是代码的一部分。

2.当我们在文本编辑器中编写代码时，千万不要自己添加 >>>。

print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出：

    >>> print 'The quick brown fox', 'jumps over', 'the lazy dog'
    The quick brown fox jumps over the lazy dog

print会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来的：

![](http://img.mukewang.com/54055502000179c205060086.jpg)

print也可以打印整数，或者计算结果：

    >>> print 300
    300#运行结果
    >>> print 100 + 200
    300#运行结果

因此，我们可以把计算100 + 200的结果打印得更漂亮一点：
    
    >>> print '100 + 200 =', 100 + 200
    100 + 200 = 300 #运行结果

因此，我们可以把计算100 + 200的结果打印得更漂亮一点：

    >>> print '100 + 200 =', 100 + 200
    100 + 200 = 300 #运行结果

注意: 对于100 + 200，Python解释器自动计算出结果300，但是，'100 + 200 ='是字符串而非数学公式，Python把它视为字符串，请自行解释上述打印结果。

## Python的注释

任何时候，我们都可以给程序加上注释。注释是用来说明代码的，给自己或别人看，而程序运行的时候，Python解释器会直接忽略掉注释，所以，有没有注释不影响程序的执行结果，但是影响到别人能不能看懂你的代码。

Python的注释以` # ` 开头，后面的文字直到行尾都算注释

`# `这一行全部都是注释...

print 'hello'` # `这也是注释
    
注释还有一个巧妙的用途，就是一些代码我们不想运行，但又不想删除，就可以用注释暂时屏蔽掉：

`#` 暂时不想运行下面一行代码:

`#` print 'hello, python.'
> 

## Python中什么是变量

在Python中，变量的概念基本上和初中代数的方程变量是一致的。
例如，对于方程式 `y=x*x` ，`x`就是变量。当`x=2`时，计算结果是`4`，当`x=5`时，计算结果是`25`。

只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

在Python程序中，变量是用一个变量名表示，变量名必须是**大小写英文、数字和下划线（_）的组合，且不能用数字开头**，比如：

    a = 1

变量a是一个整数。

    t_007 = 'T007'

变量t_007是一个字符串。

在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：

    a = 123# a是整数
    print a
    a = 'imooc'   # a变为字符串
    print a

这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。

静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下（// 表示注释）：
    
    int a = 123; // a是整数类型变量
    a = "mooc"; // 错误：不能把字符串赋给整型变量

和静态语言相比，动态语言更灵活，就是这个原因。
请不要把赋值语句的等号等同于数学的等号。比如下面的代码：

    x = 10
    x = x + 2

如果从数学上理解x = x + 2那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。

最后，理解变量在计算机内存中的表示也非常重要。当我们写：`a = 'ABC'`时，Python解释器干了两件事情：

1. 在内存中创建了一个`'ABC'`的字符串；
2. 在内存中创建了一个名为`a`的变量，并把它指向`'ABC'`。

也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

    a = 'ABC'
    b = a
    a = 'XYZ'
    print b

最后一行打印出变量b的内容到底是'ABC'呢还是'XYZ'？如果从数学意义上理解，就会错误地得出b和a相同，也应该是'XYZ'，但实际上b的值是'ABC'，让我们一行一行地执行代码，就可以看到到底发生了什么事：

最后一行打印出变量b的内容到底是'ABC'呢还是'XYZ'？如果从数学意义上理解，就会错误地得出b和a相同，也应该是'XYZ'，但实际上b的值是'ABC'，让我们一行一行地执行代码，就可以看到到底发生了什么事：
    
执行`a = 'ABC'`，解释器创建了字符串  `'ABC'`和变量 `a`，并把`a`指向 `'ABC'`：

![](http://img.mukewang.com/540581030001c11202360058.jpg)

执行`b = a`，解释器创建了变量 `b`，并把`b`指向 `a` 指向的字符串`'ABC'`：

![](http://img.mukewang.com/53fc5e880001399902360084.jpg)

执行`a = 'XYZ'`，解释器创建了字符串`'XYZ'`，并把`a`的指向改为`'XYZ'`，但`b`并没有更改：
![](http://img.mukewang.com/53fc5e9f0001b98d02360090.jpg)

执行a` = 'XYZ'`，解释器创建了字符串`'XYZ'`，并把`a`的指向改为`'XYZ'`，但`b`并没有更改：

![](http://img.mukewang.com/53fc5e9f0001b98d02360090.jpg)

所以，最后打印变量b的结果自然是`'ABC'`了。

## Python中定义字符串

前面我们讲解了什么是字符串。字符串可以用`''`或者`""`括起来表示。

如果字符串本身包含`'`怎么办？比如我们要表示字符串` I'm OK `，这时，可以用`" "`括起来表示：
    "I'm OK"

类似的，如果字符串包含`"`，我们就可以用`' '`括起来表示：

    'Learn "Python" in imooc'

如果字符串既包含`'`又包含`"`怎么办？

这个时候，就需要对字符串的某些特殊字符进行“转义”，Python字符串用`\`进行转义。

要表示字符串 `Bob said "I'm OK"`.

由于 `' `和 `"` 会引起歧义，因此，我们在它前面插入一个`\`表示这是一个普通字符，不代表字符串的起始，因此，这个字符串又可以表示为

    'Bob said \"I\'m OK\".'

注意：转义字符 \ 不计入字符串的内容中。

常用的转义字符还有：

    \n 表示换行
    \t 表示一个制表符
    \\ 表示 \ 字符本身

##Python中raw字符串与多行字符串

如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。为了避免这种情况，我们可以在字符串前面加个前缀 `r` ，表示这是一个 raw 字符串，里面的字符就不需要转义了。例如：

    r'\(~_~)/ \(~_~)/'

但是`r'...'`表示法不能表示多行字符串，也不能表示包含'和 "的字符串（为什么？）

如果要表示多行字符串，可以用`'''...'''`表示：

    '''Line 1
    Line 2
    Line 3'''

上面这个字符串的表示方法和下面的是完全一样的：

    'Line 1\nLine 2\nLine 3'

还可以在多行字符串前面添加` r `，把这个多行字符串也变成一个raw字符串：

    r'''Python is created by "Guido".
    It is free and easy to learn.
    Let's start learn Python in imooc!'''


## Python中Unicode字符串

字符串还有一个编码问题。

因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），0 - 255被用来表示大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母 A 的编码是65，小写字母 z 的编码是122。

如果要表示中文，显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。

类似的，日文和韩文等其他语言也有这个问题。为了统一所有文字的编码，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

Unicode通常用两个字节表示一个字符，原有的英文编码从单字节变成双字节，只需要把高字节全部填为0就可以。

因为Python的诞生比Unicode标准发布的时间还要早，所以最早的Python只支持ASCII编码，普通的字符串'ABC'在Python内部都是ASCII编码的。

Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示，比如：

    print u'中文'
    中文
注意: 不加 u ，中文就不能正常显示。

Unicode字符串除了多了一个 `u `之外，与普通字符串没啥区别，转义字符和多行表示法仍然有效：

转义：
    u'中文\n日文\n韩文'

多行：
    u'''第一行
    第二行'''

raw+多行：

    ur'''Python的Unicode字符串支持"中文",
    "日文",
    "韩文"等多种语言'''

如果中文字符串在Python环境下遇到` UnicodeDecodeError`，这是因为.py文件保存的格式有问题。可以在第一行添加注释

    # -*- coding: utf-8 -*-

目的是告诉Python解释器，用`UTF-8`编码读取源代码。然后用Notepad++ 另存为... 并选择`UTF-8`格式保存。


## Python中整数和浮点数
Python支持对整数和浮点数直接进行四则混合运算，运算规则和数学上的四则运算规则完全一致。

基本的运算：

    1 + 2 + 3   # ==> 6
    4 * 5 - 6   # ==> 14
    7.5 / 8 + 2.1   # ==> 3.0375
    
使用括号可以提升优先级，这和数学运算完全一致，注意只能使用小括号，但是括号可以嵌套很多层：

    (1 + 2) * 3# ==> 9
    (2.2 + 3.3) / (1.5 * (9 - 0.3))# ==> 0.42145593869731807
    
和数学运算不同的地方是，Python的整数运算结果仍然是整数，浮点数运算结果仍然是浮点数：

    1 + 2# ==> 整数 3
    1.0 + 2.0# ==> 浮点数 3.0

但是整数和浮点数混合运算的结果就变成浮点数了：

    1 + 2.0# ==> 浮点数 3.0

为什么要区分整数运算和浮点数运算呢？这是因为整数运算的结果永远是精确的，而浮点数运算的结果不一定精确，因为计算机内存再大，也无法精确表示出无限循环小数，比如` 0.1` 换成二进制表示就是无限循环小数。

那整数的除法运算遇到除不尽的时候，结果难道不是浮点数吗？我们来试一下：

    11 / 4# ==> 2

令很多初学者惊讶的是，Python的整数除法，即使除不尽，结果仍然是整数，余数直接被扔掉。不过，Python提供了一个求余的运算 % 可以计算余数：
    11 % 4# ==> 3

如果我们要计算 11 / 4 的精确结果，按照“整数和浮点数混合运算的结果是浮点数”的法则，把两个数中的一个变成浮点数再运算就没问题了：

    11.0 / 4# ==> 2.75

## Python中布尔类型

我们已经了解了Python支持布尔类型的数据，布尔类型只有True和False两种值，但是布尔类型有以下几种运算：

**与运算**：只有两个布尔值都为 True 时，计算结果才为 True。

    True and True   # ==> True
    True and False   # ==> False
    False and True   # ==> False
    False and False   # ==> False

**或运算**：只要有一个布尔值为 True，计算结果就是 True。

    True or True   # ==> True
    True or False   # ==> True
    False or True   # ==> True
    False or False   # ==> False

**非运算**：把True变为False，或者把False变为True：

    not True   # ==> False
    not False   # ==> True
    
布尔运算在计算机中用来做条件判断，根据计算结果为True或者False，计算机可以自动执行不同的后续代码。

在Python中，布尔类型还可以与其他数据类型做 and、or和not运算，请看下面的代码：

    a = True
    print a and 'a=T' or 'a=F'

计算结果不是布尔类型，而是字符串 'a=T'，这是为什么呢？

因为Python把`0、空字符串''和None`看成 `False`，`其他数值和非空字符串都`看成 `True`，所以：

    True and 'a=T' 计算结果是 'a=T'
    继续计算 'a=T' or 'a=F' 计算结果还是 'a=T'

**要解释上述结果，又涉及到 and 和 or 运算的一条重要法则：短路计算。**

1. 在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。

2. 在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。
3. 
所以Python解释器在做布尔运算时，只要能提前确定计算结果，它就不会往后算了，直接返回结果。


## Python创建list

Python内置的一种数据类型是列表：`list`。list是一种有序的集合，可以随时添加和删除其中的元素。

比如，列出班里所有同学的名字，就可以用一个list表示：

    >>> ['Michael', 'Bob', 'Tracy']
    ['Michael', 'Bob', 'Tracy']

list是数学意义上的有序集合，也就是说，list中的元素是按照顺序排列的。

构造list非常简单，按照上面的代码，直接用 [ ] 把list的所有元素都括起来，就是一个list对象。通常，我们会把list赋值给一个变量，这样，就可以通过变量来引用list：

    >>> classmates = ['Michael', 'Bob', 'Tracy']
    >>> classmates         
    ['Michael', 'Bob', 'Tracy']

由于Python是动态语言，所以list中包含的元素并不要求都必须是同一种数据类型，我们完全可以在list中包含各种数据：

    >>> L = ['Michael', 100, True]
    
一个元素也没有的list，就是空list：

    >>> empty_list = []
    

## Python按照索引访问list

由于list是一个有序集合，所以，我们可以用一个list按分数从高到低表示出班里的3个同学：

    >>> L = ['Adam', 'Lisa', 'Bart']

那我们如何从list中获取指定第 N 名的同学呢？方法是通过索引来获取list中的指定元素。

**需要特别注意的是**，索引从 0 开始，也就是说，第一个元素的索引是0，第二个元素的索引是1，以此类推。

因此，要打印第一名同学的名字，用 L[0]:

    >>> print L[0]
    Adam

要打印第二名同学的名字，用 L[1]:

    >>> print L[1]
    Lisa
    
要打印第三名同学的名字，用 L[2]:

    >>> print L[2]
    Bart
    
要打印第四名同学的名字，用 L[3]:

    >>> print L[3]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

报错了！IndexError意思就是索引超出了范围，因为上面的list只有3个元素，有效的索引是 0，1，2。

所以，使用索引时，千万注意**不要越界**。

## Python之倒序访问list

我们还是用一个list按分数从高到低表示出班里的3个同学：

    >>> L = ['Adam', 'Lisa', 'Bart']

这时，老师说，请分数最低的同学站出来。
要写代码完成这个任务，我们可以先数一数这个 list，发现它包含3个元素，因此，最后一个元素的索引是2：

    >>> print L[2]
    Bart

有没有更简单的方法？

有！

Bart同学是最后一名，俗称倒数第一，所以，我们可以用 -1 这个索引来表示最后一个元素：

    >>> print L[-1]
    Bart

Bart同学表示躺枪。

类似的，倒数第二用 -2 表示，倒数第三用 -3 表示，倒数第四用 -4 表示：

    >>> print L[-2]
    Lisa
    >>> print L[-3]
    Adam
    >>> print L[-4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

L[-4] 报错了，因为倒数第四不存在，一共只有3个元素。
  使用倒序索引时，也要注意**不要越界**。

## Python之添加新元素

现在，班里有3名同学：

    >>> L = ['Adam', 'Lisa', 'Bart']

今天，班里转来一名新同学 Paul，如何把新同学添加到现有的 list 中呢？
第一个办法是用 list 的 `append()` 方法，把新同学追加到 list 的末尾：

    >>> L = ['Adam', 'Lisa', 'Bart']
    >>> L.append('Paul')
    >>> print L
    ['Adam', 'Lisa', 'Bart', 'Paul']

append()总是把新的元素添加到 list 的尾部。
如果 Paul 同学表示自己总是考满分，要求添加到第一的位置，怎么办？

方法是用list的 insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素：

    >>> L = ['Adam', 'Lisa', 'Bart']
    >>> L.insert(0, 'Paul')
    >>> print L
    ['Paul', 'Adam', 'Lisa', 'Bart']

`L.insert(0, 'Paul') `的意思是，'Paul'将被添加到索引为 0 的位置上（也就是第一个），而原来索引为 0 的Adam同学，以及后面的所有同学，都自动向后移动一位。


## Python从list删除元素

Paul同学刚来几天又要转走了，那么我们怎么把Paul 从现有的list中删除呢？
如果Paul同学排在最后一个，我们可以用list的`pop()`方法删除：

    >>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
    >>> L.pop()
    'Paul'
    >>> print L
    ['Adam', 'Lisa', 'Bart']

pop()方法总是**删掉list的最后一个元素**，并且它还返回这个元素，所以我们执行 `L.pop()` 后，会打印出 'Paul'。

如果Paul同学不是排在最后一个怎么办？比如Paul同学排在第三：

    >>> L = ['Adam', 'Lisa', 'Paul', 'Bart']

要把Paul踢出list，我们就必须先定位Paul的位置。由于Paul的索引是2，因此，用` pop(2)`把Paul删掉：

    >>> L.pop(2)
    'Paul'
    >>> print L
    ['Adam', 'Lisa', 'Bart']

## Python中替换元素

假设现在班里仍然是3名同学：

    >>> L = ['Adam', 'Lisa', 'Bart']

现在，Bart同学要转学走了，碰巧来了一个Paul同学，要更新班级成员名单，我们可以先把Bart删掉，再把Paul添加进来。

另一个办法是直接用Paul把Bart给替换掉：

    >>> L[2] = 'Paul'
    >>> print L
    L = ['Adam', 'Lisa', 'Paul']

对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变。

由于Bart还可以用 -1 做索引，因此，下面的代码也可以完成同样的替换工作：

    >>> L[-1] = 'Paul'

## Python之创建tuple

tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。

同样是表示班里同学的名称，用tuple表示如下：

    >>> t = ('Adam', 'Lisa', 'Bart')

创建tuple和创建list唯一不同之处是用( )替代了[ ]。

现在，这个` t `就不能改变了，tuple没有 append()方法，也没有insert()和pop()方法。所以，新同学没法直接往 tuple 中添加，老同学想退出 tuple 也不行。

获取 tuple 元素的方式和 list 是一模一样的，我们可以正常使用 t[0]，t[-1]等索引方式访问元素，但是不能赋值成别的元素，不信可以试试：

    >>> t[0] = 'Paul'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

## Python之创建单元素tuple

tuple和list一样，可以包含 0 个、1个和任意多个元素。
包含多个元素的 tuple，前面我们已经创建过了。
包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示：

    >>> t = ()
    >>> print t
    ()

创建包含1个元素的 tuple 呢？来试试：

    >>> t = (1)
    >>> print t
    1

好像哪里不对！t 不是 tuple ，而是整数1。为什么呢？

因为()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果 1，导致我们得到的不是tuple，而是整数 1。

正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“`,`”，这样就避免了歧义：

    >>> t = (1,)
    >>> print t
    (1,)

Python在打印单元素tuple时，也自动添加了一个“,”，为了更明确地告诉你这是一个tuple。
多元素 tuple 加不加这个额外的“,”效果是一样的：

    >>> t = (1, 2, 3,)
    >>> print t
    (1, 2, 3)

## Python之“可变”的tuple

前面我们看到了tuple一旦创建就不能修改。现在，我们来看一个“可变”的tuple：

    >>> t = ('a', 'b', ['A', 'B'])

注意到 t 有 3 个元素：'a'，'b'和一个list：['A', 'B']。list作为一个整体是tuple的第3个元素。list对象可以通过 t[2] 拿到：

    >>> L = t[2]

然后，我们把list的两个元素改一改：

    >>> L[0] = 'X'
    >>> L[1] = 'Y'

再看看tuple的内容：

    >>> print t
    ('a', 'b', ['X', 'Y'])

不是说tuple一旦定义后就不可变了吗？怎么现在又变了？
别急，我们先看看定义的时候tuple包含的3个元素：

![](http://img.mukewang.com/540538d400010f4603500260.jpg)

当我们把list的元素'A'和'B'修改为'X'和'Y'后，tuple变为：

![](http://img.mukewang.com/540538e9000110c003500260.jpg)

表面上看，tuple的元素确实变了，但其实变的不是 tuple 的元素，而是list的元素。

tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

## Python之if语句

计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。

比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，可以用if语句实现：

    age = 20
    if age >= 18:
    print 'your age is', age
    print 'adult'
    print 'END'

注意: **Python代码的缩进规则**。具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。如果 if 语句判断为 True，就会执行这个代码块。
缩进请严格按照Python的习惯写法：**4个空格，不要使用Tab，更不要混合Tab和空格**，否则很容易造成因为缩进引起的语法错误。

注意: if 语句后接表达式，然后用`:`表示代码块开始。

如果你在**Python交互环境**下敲代码，还要特别**留意缩进** **，并且退出缩进需要多敲一行回车**：

    >>> age = 20
    >>> if age >= 18:
    ... print 'your age is', age
    ... print 'adult'
    ...
    your age is 20
    adult


## Python之 if-else

当 if 语句判断表达式的结果为 True 时，就会执行 if 包含的代码块：

    if age >= 18:
    print 'adult'

如果我们想判断年龄在18岁以下时，打印出 'teenager'，怎么办？
方法是再写一个 if:

    if age < 18:
    print 'teenager'

或者用 not 运算：

    if not age >= 18:
    print 'teenager'
    
细心的同学可以发现，这两种条件判断是“非此即彼”的，要么符合条件1，要么符合条件2，因此，完全可以用一个 `if ... else ...` 语句把它们统一起来：

    if age >= 18:
    print 'adult'
    else:
    print 'teenager'

利用 `if ... else ...` 语句，我们可以根据条件表达式的值为 True 或者 False ，分别执行 if 代码块或者 else 代码块。

注意: else 后面有个“`:`”。

## Python之 if-elif-else

有的时候，一个 if ... else ... 还不够用。比如，根据年龄的划分：

    条件1：18岁或以上：adult
    条件2：6岁或以上：teenager
    条件3：6岁以下：kid

我们可以用一个 if age >= 18 判断是否符合条件1，如果不符合，再通过一个 if 判断 age >= 6 来判断是否符合条件2，否则，执行条件3：

    if age >= 18:
    print 'adult'
    else:
    if age >= 6:
    print 'teenager'
    else:
    print 'kid'

这样写出来，我们就得到了一个两层嵌套的 `if ... else ... `语句。这个逻辑没有问题，但是，如果继续增加条件，比如3岁以下是 baby：

    if age >= 18:
    print 'adult'
    else:
    if age >= 6:
    print 'teenager'
    else:
    if age >= 3:
    print 'kid'
    else:
    print 'baby'

这种缩进只会越来越多，代码也会越来越难看。

要避免嵌套结构的` if ... else ...`，我们可以用` if ... `多个`elif ... else ... `的结构，一次写完所有的规则：

    if age >= 18:
    print 'adult'
    elif age >= 6:
    print 'teenager'
    elif age >= 3:
    print 'kid'
    else:
    print 'baby'

elif 意思就是 else if。这样一来，我们就写出了结构非常清晰的一系列条件判断。

特别注意: 这一系列条件判断会从上到下依次判断，如果某个判断为 True，执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。


## Python之 for循环
 
list或tuple可以表示一个有序集合。如果我们想依次访问一个list中的每一个元素呢？比如 list：

    L = ['Adam', 'Lisa', 'Bart']
    print L[0]
    print L[1]
    print L[2]
    
如果list只包含几个元素，这样写还行，如果list包含1万个元素，我们就不可能写1万行print。

这时，循环就派上用场了。

Python的 for 循环就可以依次把list或tuple的每个元素迭代出来：

    L = ['Adam', 'Lisa', 'Bart']
    for name in L:
    print name
    
注意:  name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。

这样一来，遍历一个list或tuple就非常容易了。

## Python之 while循环

和 for 循环不同的另一种循环是 while 循环，while 循环不会迭代 list 或 tuple 的元素，而是根据表达式判断循环是否结束。

比如要从 0 开始打印不大于 N 的整数：

    N = 10
    x = 0
    while x < N:
    print x
    x = x + 1
    
while循环每次先判断 x < N，如果为True，则执行循环体的代码块，否则，退出循环。
在循环体内，x = x + 1 会让 x 不断增加，最终因为 x < N 不成立而退出循环。
如果没有这一个语句，while循环在判断 x < N 时总是为True，就会无限循环下去，变成死循环，所以要特别留意while循环的退出条件。

## Python之 break退出循环
用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。
比如计算1至100的整数和，我们用while来实现：

    sum = 0
    x = 1
    while True:
    sum = sum + x
    x = x + 1
    if x > 100:
    break
    print sum

咋一看， while True 就是一个死循环，但是在循环体内，我们还判断了 x > 100 条件成立时，用break语句退出循环，这样也可以实现循环的结束。

## Python之 continue继续循环

在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。

假设我们已经写好了利用for循环计算平均分的代码：

    L = [75, 98, 59, 81, 66, 43, 69, 85]
    sum = 0.0
    n = 0
    for x in L:
    sum = sum + x
    n = n + 1
    print sum / n

现在老师只想统计及格分数的平均分，就要把 x < 60 的分数剔除掉，这时，利用 continue，可以做到当 x < 60的时候，不继续执行循环体的后续代码，直接进入下一次循环：

    for x in L:
    if x < 60:
    continue
    sum = sum + x
    n = n + 1

## Python之 多重循环
  在循环内部，还可以嵌套循环，我们来看一个例子：
 
    for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
    print x + y

x 每循环一次，y 就会循环 3 次，这样，我们可以打印出一个全排列：


    A1
    A2
    A3
    B1
    B2
    B3
    C1
    C2
    C3
    

## Python之什么是dict
 我们已经知道，list 和 tuple 可以用来表示顺序集合，例如，班里同学的名字：

    ['Adam', 'Lisa', 'Bart']

或者考试的成绩列表：

    [95, 85, 59]

但是，要根据名字找到对应的成绩，用两个 list 表示就不方便。

如果把名字和分数关联起来，组成类似的查找表：

    'Adam' ==> 95
    'Lisa' ==> 85
    'Bart' ==> 59

给定一个名字，就可以直接查到分数。

Python的 dict 就是专门干这件事的。用 dict 表示“名字”-“成绩”的查找表如下：

    d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
    }

我们把名字**称为key**，对应的成绩**称为value**，dict就是通过 key 来查找 value。
花括号 **{}**表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。

由于dict也是集合，`len()` 函数可以计算任意集合的大小：

    >>> len(d)
    3

注意: 一个 key-value 算一个，因此，dict大小为3。

## Python之访问dict

我们已经能创建一个dict，用于表示名字和成绩的对应关系：

    d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
    }

那么，如何根据名字来查找对应的成绩呢？

可以简单地使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict使用key：

    >>> print d['Adam']
    95
    >>> print d['Paul']
    Traceback (most recent call last):
      File "index.py", line 11, in <module>
    print d['Paul']
    KeyError: 'Paul'

注意: 通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。

要避免 KeyError 发生，有两个办法：

一是先判断一下 key 是否存在，用 in 操作符：

    if 'Paul' in d:
    print d['Paul']

如果 'Paul' 不存在，if语句判断为False，自然不会执行 print d['Paul'] ，从而避免了错误。

二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：

    >>> print d.get('Bart')
    59
    >>> print d.get('Paul')
    None


## Python中dict的特点
**dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降**。

不过dict的查找速度快不是没有代价的，**dict的缺点是占用内存大，还会浪费很多内容，**list正好相反，占用内存小，但是查找速度慢。


由于dict是按 key 查找，所以，在一个dict中，**key不能重复**。

**dict的第二个特点就是存储的key-value序对是没有顺序的！**这和list不一样：

    d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
    }

当我们试图打印这个dict时：

    >>> print d
    {'Lisa': 85, 'Adam': 95, 'Bart': 59}

打印的顺序不一定是我们创建时的顺序，而且，不同的机器打印的顺序都可能不同，这说明dict内部是无序的，不能用dict存储有序的集合。

**dict的第三个特点是作为 key 的元素必须不可变**，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。

可以试试用list作为key时会报什么样的错误。
不可变这个限制仅作用于key，value是否可变无所谓：

    {
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
    }

最常用的key还是字符串，因为用起来最方便。



## Python更新dict

dict是可变的，也就是说，我们可以随时往dict中添加新的 key-value。比如已有dict：

    d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
    }

要把新同学'Paul'的成绩 72 加进去，用赋值语句：

    >>> d['Paul'] = 72

再看看dict的内容：

    >>> print d
    {'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 59}


如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value：

    >>> d['Bart'] = 60
    >>> print d
    {'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 60}



## Python之 遍历dict

由于dict也是一个集合，所以，遍历dict和遍历list类似，都可以通过 for 循环实现。

直接使用for循环可以遍历 dict 的 key：
    
    >>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
    >>> for key in d:
    ... print key
    ... 
    Lisa
    Adam
    Bart

由于通过 key 可以获取对应的 value，因此，在循环体内，可以获取到value的值。

## Python中什么是set

dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。

有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。

**set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。**


创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：

    >>> s = set(['A', 'B', 'C'])

可以查看 set 的内容：

    >>> print s
    set(['A', 'C', 'B'])

请注意，上述打印的形式类似 list， 但它不是 list，仔细看还可以发现，打印的顺序和原始 list 的顺序有可能是不同的，因为set内部存储的元素是无序的。

**因为set不能包含重复的元素，所以，当我们传入包含重复元素的 list 会怎么样呢？**

    >>> s = set(['A', 'B', 'C', 'C'])
    >>> print s
    set(['A', 'C', 'B'])
    >>> len(s)
    3

结果显示，set会自动去掉重复的元素，原来的list有4个元素，但set只有3个元素。

## Python之 访问set

由于set存储的是无序集合，所以我们没法通过索引来访问。
访问 set中的某个元素实际上就是判断一个元素是否在set中。
例如，存储了班里同学名字的set

    >>> s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
我们可以用 in 操作符判断：
Bart是该班的同学吗？

    >>> 'Bart' in s
    True
    
Bill是该班的同学吗？

    >>> 'Bill' in s
    False

bart是该班的同学吗？

    >>> 'bart' in s
    False

看来大小写很重要，'Bart' 和 'bart'被认为是两个不同的元素。


## Python之 set的特点

set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

最后，**set存储的元素也是没有顺序的。**
set的这些特点，可以应用在哪些地方呢？
星期一到星期日可以用字符串'MON', 'TUE', ... 'SUN'表示。
假设我们让用户输入星期一至星期日的某天，如何判断用户的输入是否是一个有效的星期呢？
可以用 if 语句判断，但这样做非常繁琐：

    x = '???' # 用户输入的字符串
    if x!= 'MON' and x!= 'TUE' and x!= 'WED' ... and x!= 'SUN':
    print 'input error'
    else:
    print 'input ok'

注意：if 语句中的...表示没有列出的其它星期名称，测试时，请输入完整。
如果事先创建好一个set，包含'MON' ~ 'SUN'：

    weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])

再判断输入是否有效，只需要判断该字符串是否在set中：

    x = '???' # 用户输入的字符串
    if x in weekdays:
    print 'input ok'
    else:
    print 'input error'

这样一来，代码就简单多了。

## Python之 遍历set

由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现。
直接使用 for 循环可以遍历 set 的元素：

    >>> s = set(['Adam', 'Lisa', 'Bart'])
    >>> for name in s:
    ... print name
    ... 
    Lisa
    Adam
    Bart

注意: 观察 for 循环在遍历set时，元素的顺序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。

## Python之 更新set

由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：

一是把新的元素添加到set中，二是把已有元素从set中删除。
添加元素时，用set的add()方法：

    >>> s = set([1, 2, 3])
    >>> s.add(4)
    >>> print s
    set([1, 2, 3, 4])

如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了：

    >>> s = set([1, 2, 3])
    >>> s.add(3)
    >>> print s
    set([1, 2, 3])

删除set中的元素时，用set的remove()方法：

    >>> s = set([1, 2, 3, 4])
    >>> s.remove(4)
    >>> print s
    set([1, 2, 3])
    
如果删除的元素不存在set中，remove()会报错：

    >>> s = set([1, 2, 3])
    >>> s.remove(4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 4

所以用add()可以直接添加，而remove()前需要判断。
