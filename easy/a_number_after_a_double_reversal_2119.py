# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
给定一个数字，先取反，然后在取反。
每次取反需要去掉引导零
这里直接通过[::-1]进行处理即可
"""


class ANumberAfterADoubleReversal(object):

    def isSameAfterReversals(self, num: int) -> bool:
        return num == int(str(int(str(num)[::-1]))[::-1])



