#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-05 19:24
# @Author: jiaxiong
# @File  : StudentSenior.py

from clazz.stuclazz import Student


class StudentSenior(Student):
    def __init__(self, name, sex, province, grade):
        super(StudentSenior, self).__init__(name, sex, province, grade)
        # Student.__init__(self,name, sex, province,grade)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return ("我不告诉你Girl名")
