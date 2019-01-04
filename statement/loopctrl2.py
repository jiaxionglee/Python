#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-04 23:34
# @Author: jiaxiong
# @File  : loopctrl2.py

age = 0
while age < 7:
    age = age + 1
    if age - 1 < 2:
        print('我还在 ', age - 1, "我要抱抱")
        continue
    print('我还在 ', age - 1, " 岁，我不上学")
