#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : list.py

myList = [1, 2, 3, 4, 1]
myList1 = [5, 6, 7, 8]
myList2 = ['python', 1, 2, 3]

print(myList + myList1)
print(myList * 2)

print(myList.index(4))

print(myList[1:])
print(myList[-3:])
print(myList[:3])
print(myList[:-3])

myList2.append(9)
print(myList2)
myList2.extend(myList1)
# 不能直接写在print里面，需要先append或extend
print(myList2.append(9))
print(myList2)

print(myList.count(1))

myList2.insert(-1, 9)
print(myList2)

myList2.pop(2)
print(myList2)
myList2.remove('python')
print(myList2)

myList2.reverse()
print(myList2)

myList2.sort()
print(myList2)


print(myList2.__len__())
