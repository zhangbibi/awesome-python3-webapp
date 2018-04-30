#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, functools


__author__ = 'zhangyaping'

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now(*args, **kw):
    print('2015-3-25', args, kw)

# now(1,2,3,age=12,sex=1)

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s is executed %s ms' % (fn.__name__, (end - start)/1000))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')