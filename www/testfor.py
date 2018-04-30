#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    maxL = L[0]
    minL = L[0]
    for x in L:
        if x > maxL:
            maxL = x
        if x < minL:
            minL = x
    return (minL, maxL)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


LL=[22,2,33,4,5,6]
for k, v in enumerate(LL):
    print(k,v)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ind.lower() for ind in L1 if isinstance(ind, str) == True]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')