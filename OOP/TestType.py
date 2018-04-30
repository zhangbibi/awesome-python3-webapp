#!/usr/bin/env python3

from TestProperties import Student

# type() 函数可以用来查看类型
s = Student(2009)
print(type(Student))
print(type(s))


# type() 还可以用来动态创建类型
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。


def fn(self, name = 'default'):
    self.name = name
    print(self.name)

TT = type('TT', (object,), dict(printName = fn))
tt = TT()

tt.printName('zhang')

