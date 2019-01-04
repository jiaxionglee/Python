#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-04 23:22
# @Author: jiaxiong
# @File  : loop4.py

for first_number in range(1, 10):
    for second_number in range(1, first_number + 1):
        print(first_number, "*", second_number, "=", first_number * second_number, end='  ')
    print("\n")
