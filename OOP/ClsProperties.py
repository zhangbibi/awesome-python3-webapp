#!/usr/bin/env python3
class Student:
    sdudentCount = 0
    def __init__(self, name):
        self.__name = name
        Student.sdudentCount = Student.sdudentCount+1
if Student.sdudentCount!=0:
    print("fail")
else:
    s1 = Student('s1')
    if Student.sdudentCount != 1:
        print('fail')
    else:
        print('students:', Student.sdudentCount)
        print('success')