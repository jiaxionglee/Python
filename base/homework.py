#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-04 21:47
# @Author: jiaxiong
# @File  : homework.py


# 作业1.1
# 安装requests模块
# sudo pip install requests
# sudo pip3 install requests
# 验证
import requests

print(requests.get('https://www.baidu.com'))

# 作业1.2
x = 2.918
print(type(x))
y = int(2.918)
print(type(y))
# 作业1.3
x = bin(int('18', 10))
print(x)
# 作业1.4
my_str = "Python is popular"
my_str_new = my_str.replace('Python', 'JAVA')
print(my_str_new)
# 作业1.5
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[1::2])
# 作业1.6
my_dic = {"name": "xiaoming", "sex": "male", "province": "beijing"}
print(my_dic)
my_dic["province"] = "江苏"
print(my_dic)

# 作业2.1
my_str = "Python was created in 1989, Python is using in AI, big data, IOT."
print("所有大写转小写")
print(my_str.lower())
print("单词放到列表，不包含空格")
my_str_list = my_str.split()
print(my_str_list)
print("打印列表最中间单词")
pos = my_str_list.__len__() / 2
print(my_str_list.pop(int(pos)))

# 作业2.2
list1 = ['python', 5, 6, 8]
list2 = ['python', '5', 6, 8, 10]

print(list1 + list2)
list3 = list(set(list1 + list2))
print(type(list3))
print(list3)
