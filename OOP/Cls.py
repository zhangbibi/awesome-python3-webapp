#!/usr/bin/env python3

class Student(object):
    def __init__(self, age, score):
        self.__age = age
        self.__score = score



    def __str__(self):
        return self.__age + " : "+ self.__score

    def getGrade(self):
        if self.__score>60:
            return 'A'
        else:
            return 'B'

stu = Student(12,68)
print(stu.getGrade())

print(stu.__age)