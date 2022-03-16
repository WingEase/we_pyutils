#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : ip.py
@Time    : 2022/3/15 8:48
@Author  : ZENKR
@Email   : zenkr@qq.com
@Software: PyCharm
@Desc    :
@license : Copyright (c) 2022 WingEase Technology Co.,Ltd. All Rights Reserved.
"""
import unittest

from we_pyutils.ip import get_my_ip


class IPTestCase(unittest.TestCase):
    def test_get_my_ip(self):
        ip = get_my_ip()
        self.assertTrue(ip)


if __name__ == '__main__':
    unittest.main()
