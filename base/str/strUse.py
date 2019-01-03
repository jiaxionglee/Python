#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : strUse.py

s = 'I Love Python'
s1 = " , and you ?"

# 串联多个字符串
print(s + s1)
# 快速复制字符串
print(s * 2)
# 分割字符串
s2 = s.split(' ', 2)
print(s2)
# 替换字符串
s_replace = s.replace('Python', 'Java')
print(s_replace)
# 转大写
s_upper = s.upper()
print(s_upper)
# 转小写
s_lower = s.lower()
print(s_lower)
# 首字母大写
print('sss'+s_lower.capitalize())
# 字符串查找
s_index = s.index('ov')
print(s_index)

print(s.encode().decode())
print(s.startswith('I'))
print(s.endswith('o'))
print(s.__len__())
print(s.isdigit())
s3 = '  i test python  '
print(s3)
print(s3.strip())
