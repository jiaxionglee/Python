#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-05 17:00
# @Author: jiaxiong
# @File  : exception.py


try:
    print("Hello World")
except:
    print("This is an error message!")

x = 10
y = 0
try:
    result = x / y
# except ZeroDivisionError:
#     print("除数不能为0")
except Exception as e:
    print(e)
else:
    print("结果是：", result)
finally:
    print("任何情况下都有我的存在")
