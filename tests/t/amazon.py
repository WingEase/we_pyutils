#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : amazon.py
@Time    : 2020-02-11 21:07
@Author  : ZENKR
@Email   : zenkr@qq.com
@Software: PyCharm
@Desc    :
@license : Copyright (c) 2020 WingEase Technology Co.,Ltd. All Rights Reserved.
"""
import unittest
from decimal import Decimal, getcontext

from we_pyutils.t.amazon import extract_price, extract_star


class TestAmazon(unittest.TestCase):
    """测试Amazon"""

    def test_extract_star(self):
        self.assertEqual(4.6, extract_star('4.6 of 5'))
        self.assertEqual(4, extract_star('4 of 5'))
        self.assertEqual(4.6, extract_star('4,6 of 5'))
        self.assertEqual(0, extract_star('0 of 5'))
        self.assertEqual(5, extract_star('5 of 5'))
        self.assertEqual(None, extract_star(''))

    def test_extract_price(self):
        """Test method extract_price('£0.99')"""
        precision = 2
        getcontext().prec = precision
        self.assertEqual(Decimal('1222333.00'), extract_price('$ 1,222,333'))
        self.assertEqual(Decimal('1222333.99'), extract_price('£1,222,333.99'))
        self.assertEqual(Decimal('0.99'), extract_price('£0.99'))
        self.assertEqual(Decimal('1222333.00'), extract_price('1.222.333€', '.', ','))
        self.assertEqual(Decimal('1222333.99'), extract_price('1.222.333,99 €', '.', ','))
        self.assertEqual(Decimal('0.99'), extract_price('0,99', '.', ','))
        self.assertEqual(None, extract_price(''))


if __name__ == '__main__':
    unittest.main()
