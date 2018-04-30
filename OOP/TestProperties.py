#!/usr/bin/env python3

#Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student(object):
    def __init__(self, bir):
        self.birth = bir

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

s = Student(2018)
print(s.birth)
s.birth=2019
print(s.birth)