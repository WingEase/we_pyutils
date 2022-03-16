#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : proxy_test.py
@Time    : 2021/3/28 16:55
@Author  : ZENKR
@Email   : zenkr@qq.com
@Software: PyCharm
@Desc    :
@license : Copyright (c) 2021 WingEase Technology Co.,Ltd. All Rights Reserved.
"""

import unittest

from we_pyutils.proxy.ty import ProxyIP, ProxyIPPool


class TYProxyTest(unittest.TestCase):
    """
    太阳代理测试
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_proxy_ip(self):
        ip_1_dict = {
            "city": "吉林省四平市",
            "expire_time": "2021-03-22 11:11:11",
            "ip": "127.0.0.1",
            "isp": "联通",
            "port": "1111"
        }
        ip_2_dict = {
            "city": "吉林省四平市",
            "expire_time": "2021-03-22 22:22:22",
            "ip": "127.0.0.2",
            "isp": "联通",
            "port": 2222
        }
        ip_3_dict = {
            "city": "吉林省四平市",
            "expire_time": "2021-03-22 00:00:33",
            "ip": "127.0.0.3",
            "isp": "联通",
            "port": 3333
        }
        ip_1 = ProxyIP(ip_dict=ip_1_dict)
        ip_2 = ProxyIP(ip_dict=ip_2_dict)
        ip_3 = ProxyIP(ip_dict=ip_3_dict)
        ip_1_expire_time = ProxyIP.format_expire_time("2021-03-22 11:11:11")
        ip_1b = ProxyIP('127.0.0.1', 1111, ip_1_expire_time, isp='联通', city='吉林省四平市')
        ip_1c = ProxyIP('127.0.0.1', 1111, "2021-03-22 11:11:11", isp='联通', city='吉林省四平市')
        self.assertEqual(ip_1, ip_1b)
        self.assertEqual(ip_1b, ip_1c)
        self.assertEqual(f'{ip_1b.ip}:{ip_1b.port}', ip_1b.use_ip_str())

        ip_list_1 = [
            ip_1_dict, ip_2_dict, ip_3_dict
        ]
        ip_pool_1_dict = {
            "127.0.0.1": ip_1,
            "127.0.0.2": ip_2,
            "127.0.0.3": ip_3
        }
        ip_pool_1 = ProxyIPPool()
        ip_pool_1.enlarge_ip_pool_b(ip_list_1)
        self.assertEqual(ip_pool_1_dict, ip_pool_1.get_ip_pool())

        self.assertIsInstance(ip_pool_1.random_choice_ip(), ProxyIP)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
