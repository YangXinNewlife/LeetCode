# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
from math import ceil
"""
Solutions:
本题的题意是给出字符串A和B，让A变成n倍，看看B是否有可能成为A的子串；
这个时候我们要选出N的取值范围，然后一次判断即可。其实我们只要计算两者的字符串的长度公约数，
并向上取整为下限，然后上限为下限 + 1即可；
"""


class RepeatedStringMatch(object):

    def repeatedStringMatch(self, A: str, B: str) -> int:
        n_low = int(ceil(len(B) / len(A)))
        n_high = n_low + 1
        if B in A * n_low:
            return n_low
        elif B in A * n_high:
            return n_high
        return -1

