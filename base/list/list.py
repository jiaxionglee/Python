#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : list.py

myList = [1, 2, 3, 4, 1]
myList1 = [5, 6, 7, 8]

print(myList + myList1)
print(myList * 2)

print(myList.index(4))

print(myList[1:])
print(myList[-3:])
print(myList[:3])
print(myList[:-3])

print(myList.append(9))
