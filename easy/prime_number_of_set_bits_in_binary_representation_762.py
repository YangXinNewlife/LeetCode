# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：
我们输入两个边界L和R，我们要在 L 到 R 的数据中找出每个元素的二进制表示中，1 的格式是否为素数的情况下有几个；
其中int型总共32位，那么最多找出小于32的素数就可以了；
"""


class PrimeNumberOfSetBitsInBinaryRepresentation(object):

    def countPrimeSetBits(self, L: int, R: int) -> int:
        result = 0
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for i in range(L, R + 1):
            num = bin(i)
            count = num.count('1')
            if count in prime_list:
                result += 1
        return result

