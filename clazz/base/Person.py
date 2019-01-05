#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-05 19:07
# @Author: jiaxiong
# @File  : Person.py


class Person:
    total_person = 0

    def __init__(self, name, sex, province):
        print("Init the clazz")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
