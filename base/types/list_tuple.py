#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-03 20:24
# @Author: jiaxiong
# @File  : list_tuple.py

# list to tuple
myList = [1, 2, 3, 4, 1]
print(myList)
print(type(myList))
myList_tp = tuple(myList)
print(myList_tp)
print(type(myList_tp))

print('*'*20)
# tuple to list
myTuple = (5, 6, 7, 8, 5)
print(myTuple)
print(type(myTuple))
myTuple_l = list(myTuple)
print(myTuple_l)
print(type(myTuple_l))
