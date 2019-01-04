#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-04 23:19
# @Author: jiaxiong
# @File  : loop3.py

companies = ['google', 'baidu', 'ali', "taobao"]
for index in range(len(companies)):
    print(companies[index])
    if companies[index] == "google":
        print("google 是个不作恶 的公司")
    elif companies[index] == "baidu":
        print("中国搜索公司")
    else:
        print("非搜索引擎公司")
