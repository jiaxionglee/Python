#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : homework.py

# 1.1
for x in range(1000, 2500):
    if x % 7 == 0:
        if x % 5 == 0:
            print(x)

# 1.2
for x in range(0, 20):
    if x == 0:
        continue
    if x % 3 == 0:
        if x % 5 == 0:
            print('three+fives')
        else:
            print('three')
    elif x % 5 == 0:
        print('five')
    else:
        print(x)
