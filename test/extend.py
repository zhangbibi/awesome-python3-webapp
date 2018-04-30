#!/usr/bin/env python3

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('dog is running...')

class Cat(Animal):
    def run(self):
        print('cat is running...')



class Timer(object):
    def run(self):
        print('timer is running...')

def testRun(a):
    a.run()
    a.run()

testRun(Animal())
testRun(Dog())
testRun(Timer())