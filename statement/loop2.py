#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-04 23:16
# @Author: jiaxiong
# @File  : loop2.py

companies = ['google', 'baidu', 'ali', "taobao"]
for company in companies:
    print(company)
    if company == "google":
        print("google 是个不作恶 的公司")
    elif company == "baidu":
        print("中国搜索公司")
    else:
        print("非搜索引擎公司")
