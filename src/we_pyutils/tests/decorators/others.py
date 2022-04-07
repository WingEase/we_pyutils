#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : others.py
@Time    : 2022/3/17 20:41
@Author  : ZENKR
@Email   : zenkr@qq.com
@Software: PyCharm
@Desc    :
@license : Copyright (c) 2022 WingEase Technology Co.,Ltd. All Rights Reserved.
"""
import unittest

# from we_pyutils.ip import get_my_ip
from we_pyutils.decorators.others import singleton


class SingletonTestCase(unittest.TestCase):
    def test_singleton_decorator(self):
        @singleton()
        class A:
            a = 10

        @singleton()
        class B:
            b = 10

        a1 = A()
        self.assertEqual(10, a1.a)
        a1.a = 11
        self.assertEqual(11, a1.a)
        a2 = A()
        self.assertEqual(11, a2.a)
        a2.a = 12
        self.assertEqual(12, a2.a)
        self.assertEqual(12, a1.a)

    def test_singleton_decorator_with_params(self):
        pass


if __name__ == '__main__':
    unittest.main()
