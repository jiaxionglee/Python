#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-04 23:23
# @Author: jiaxiong
# @File  : loop5.py

wid = 1
while wid <= 5:
    myLen = 1
    while myLen <= wid:
        print("*", ' ', end='')
        myLen += 1
    print("\n")
    wid += 1
