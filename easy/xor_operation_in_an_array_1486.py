# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数组大小 n 和计算的标识 start
然后分别计算每个元素的值 (start + 2 * i)
然后分别对他们做 异或（XOR）计算即可 
"""


class XOROperationInAnArray(object):

    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            if i > 0:
                result = result ^ (start + 2 * i)
            else:
                result = start + 2 * i
        return result
