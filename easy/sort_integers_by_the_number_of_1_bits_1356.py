# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是对给定的每个值转换二进制后，统计里面的1的个数，由低到高升序排列。
可以直接使用lambda x: (bin(x).count("1")统计1的个数即可，
bin是转换二进制的方式。
"""


class SortIntegersByTheNumberOf1Bits(object):

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))

