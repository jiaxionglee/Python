#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-02 22:52
# @Author: jiaxiong
# @File  : dict.py


my_dic = {"name": "xiaozhang", "company": "baidu", "grade": "T7"}
my_dic2 = {"name1": "wangwu", "company1": "tengxun", "grade1": "T3"}


# 合并多个dict，key值需要不一致
my_dic.update(my_dic2)
# print(my_dic + my_dic2)
print(my_dic)

# 插入key
my_dic['sex'] = 'male'
print(my_dic)
# 通过key访问
print(my_dic["name"])

del my_dic['name']
print(my_dic)

print(my_dic.get('sex'))
print(my_dic.keys())
print(my_dic.values())
print(my_dic.pop('sex'))
print(my_dic.items())
print(my_dic.__iter__())




