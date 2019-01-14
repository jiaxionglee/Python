#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-01-06 16:14
# @Author: jiaxiong
# @File  : test_parameter.py


import pytest


@pytest.mark.parametrize("x,y", [
    (3 + 5, 9),
    (2 + 4, 6),
    (6 * 9, 42),
])
def test_add(x, y):
    assert x == y
