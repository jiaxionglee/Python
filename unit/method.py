#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-06 15:09
# @Author: jiaxiong
# @File  : method.py

import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self):
        print('setUp method')
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print('test_1st')
        self.assertEqual(self.foo.pop(), 9)

    def test_2nd(self):
        print('test_2nd')
        self.assertEqual(self.foo.pop(), 9)

    def tearDown(self):
        print('end method')


if __name__ == '__main__':
    unittest.main()
