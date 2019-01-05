#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-05 17:36
# @Author: jiaxiong
# @File  : homework2.py

# 2.1


def list_sum(my_list):
    result = 0
    for x in my_list:
        if str(x).isdigit():
            result += x
    return result


# 2.2
dic = {'name': 'xiaozhang', 'sex': 'male'}
try:
    print(dic['grade'])
except Exception as e:
    raise
