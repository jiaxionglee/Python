#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : if.py

# statement1
age = 18
if age >= 18:
    print('我年轻力壮')
else:
    print("我还是个孩子")

# statement2
age = int(input("请输入 年龄:"))
if age >= 18:
    print("我年轻力壮")
elif age >= 6:
    print("我还是个孩子")
elif age >= 0:
    print("我是小宝宝")
else:
    print("我不是人")

# statement3
age = 18
sex = "M"
if sex == "F":
    print("我是女孩子")
    if age >= 16:
        print("二八年华")
    elif age >= 13:
        print("豆蔻年华")
    elif age >= 0:
        print("我是女宝宝")
elif sex == "M":
    print("我是男孩子")
else:
    print("我是大猩猩")
