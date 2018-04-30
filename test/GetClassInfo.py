#!/usr/bin/env python3

import types

class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name

    def __len__(self):
        return 3

stu = Student('zyp', 23)
print(stu)

# type
print(type(stu))

# isinstance
print(isinstance(stu, Student))

# dir获取对象所有属性与方法

print(dir(stu))

#hasattr getattr setattr
print(hasattr(stu, 'name'))
print(getattr(stu, 'name'))
setattr(stu, '__name', 'hello')
print(getattr(stu, '__name'))

