#!/usr/bin/env python3

#solts 设置只允许进行绑定的参数

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'M'
s.age=22

print(s.name)

