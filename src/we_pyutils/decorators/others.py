#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : others.py
@Time    : 2022/3/16 11:51
@Author  : ZENKR
@Email   : zenkr@qq.com
@Software: PyCharm
@Desc    :
@license : Copyright (c) 2022 WingEase Technology Co.,Ltd. All Rights Reserved.
"""
from functools import wraps


class Singleton(object):
    """
    单例模式（非线程安全）
    """
    _instance: object

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


def singleton(cls):
    """
    单例模式装饰器（非线程安全）
    :param cls:
    :return:
    """
    _instance = {}

    @wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


if __name__ == '__main__':
    @singleton
    class A:
        t = 1
        pass
