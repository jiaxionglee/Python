#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-06 15:56
# @Author: jiaxiong
# @File  : test_add.py

import pytest
import time
import random


def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3


def test_add1():
    assert add(1, 2) == 3


def test_add3():
    time.sleep(random.randint(2, 6))
    pytest.assume(add('test', 'home.com') == 'testhome.com')
    pytest.assume(add(1, 2) == 3)
