# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
想要计算数据的二进制补码，
解决思路是先变成二进制，然后用1减去每一位进行翻转即可
"""


class NumberComplement(object):

    def findComplement(self, num: int) -> int:
        num_bin = bin(num)[2:]
        result = ''
        for i in num_bin:
            r = str(1 - int(i))
            result += r
        return int(result, 2)

