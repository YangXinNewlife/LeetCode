# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数字n(基于10进制)
希望我们可以将10进制的数据转化为k进制的数据
并且每位相加返回最后的和
"""


class SumOfDigitsInBaseK(object):

    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n > 0:
            result += n % k
            n //= k
        return result


# 测试部分
a = SumOfDigitsInBaseK()
a.sumBase(34, 6)
