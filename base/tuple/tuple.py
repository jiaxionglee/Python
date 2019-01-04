#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : tuple.py

my_tuple = ('python', 12, 2.3, 9.7, 12, 3, 12)
my_tuple1 = ('java', 12, 2.3, 9.7)
my_tuple2 = (('python', 12, 2.3, 9.7), ('java', 12, 2.3, 9.7))

print(my_tuple + my_tuple1)
print(my_tuple * 2)

print(my_tuple.index(12, 1, 4))
# 等步长访问
print(my_tuple[1::2])
print(my_tuple.index(12))
print(my_tuple.count(12))
