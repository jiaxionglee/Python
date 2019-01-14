#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-06 14:57
# @Author: jiaxiong
# @File  : pyunitdemo.py.py


import unittest


def add(x, y):
    return x + y


class TAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add1(self):
        self.assertEqual(add(1, 3), 4)
