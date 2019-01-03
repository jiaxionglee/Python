#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : type.py

a = 10
print(type(a))

print('*' * 30)

x_2 = '1011'
print(type(x_2))
# 二进制转八进制
x_2_8 = oct(int(x_2, 2))
print(x_2_8)
# print(type(x_2_8))
# 二进制转十进制
x_2_10 = int(x_2, 2)
print(x_2_10)
# 二进制转十六进制
x_2_16 = hex(int(x_2, 2))
print(x_2_16)

print('*' * 30)

x_8 = '0o13'
# 八进制转二进制
x_8_2 = bin(int(x_8, 8))
print(x_8_2)
# 八进制转十进制
x_8_10 = int(x_8, 8)
print(x_8_10)
# 八进制转十六进制
x_8_16 = hex(int(x_8, 8))
print(x_8_16)

print('*' * 30)

x_10 = '11'
# 十进制转二进制
x_10_2 = bin(int(x_10, 10))
print(x_10_2)
# 十进制转八进制
x_10_8 = oct(int(x_10, 10))
print(x_10_8)
# 十进制转十六进制
x_10_16 = hex(int(x_10, 10))
print(x_10_16)

print('*' * 30)

x_16 = '0xb'
# 十六进制转二进制
x_16_2 = bin(int(x_16, 16))
print(x_16_2)
# 十六进制转八进制
x_16_8 = oct(int(x_16, 16))
print(x_16_8)
# 十六进制转十进制
x_16_10 = int(x_16, 16)
print(x_16_10)
