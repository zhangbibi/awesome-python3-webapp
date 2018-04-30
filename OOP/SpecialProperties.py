#!/usr/bin/env python3

# __str__ , __repr__   打印对象信息

class Student():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student name = %s' % self.name

    __repr__ = __str__


stu = Student('zhang')

print(stu)


# __iter__

