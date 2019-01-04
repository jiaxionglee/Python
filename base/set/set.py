#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : set.py

my_set = {1, 2, 3, 5,1}
# 创建空set
my_set1 = set()
my_set2 = {1, 2, 3, 4, 1}
print(type(my_set1))

print(my_set)

# 合并
print(my_set.union(my_set2))

# 获取两个set的交集
print('*' * 10)
print(my_set.intersection(my_set2))
# 差集
print(my_set.difference(my_set2))
print('*' * 10)
# 对称差
print(my_set.symmetric_difference(my_set2))
# my_set.pop()
print(my_set)

my_set.discard(9)
print(my_set)

my_set.add(5)
print(my_set)
