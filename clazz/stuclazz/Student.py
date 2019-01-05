#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-05 19:10
# @Author: jiaxiong
# @File  : Student.py

from clazz.base import Person


class Student(Person):
    def __init__(self, name, sex, province, grade):
        super(Student, self).__init__(name, sex, province)
        # Person.__init__(self,name, sex, province)
        self.grade = grade

    def get_grade(self):
        return self.grade
