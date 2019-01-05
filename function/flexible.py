#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-05 18:04
# @Author: jiaxiong
# @File  : flexible.py


def flexible(aa, *args, **kwargs):
    mydic = {}
    mylist = []
    for x in args:
        # if aa
        mylist.append(x)
    for key, value in kwargs.items():
        mydic[key] = value
    return tuple(mylist), mydic


# print(flexible('aa', 1, x=4))
print(flexible('aa', 2, 3, x=4, y=5, *[1, 2, 3], **{'a': 1, 'b': 2}))
