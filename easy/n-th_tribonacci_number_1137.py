# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是斐波那且数列的换种，难点在于数据的范围，正常的递归逻辑肯定会超时
因此我们把每次的计算结果都存下来，避免浪费的计算。
"""


class NthTribonacciNumber(object):

    def tribonacci(self, n: int) -> int:
        result = list()
        result.append(0)
        result.append(1)
        result.append(1)
        if n <= 2:
            return result[n]
        for i in range(3, n + 1):
            temp = result[i - 1] + result[i - 2] + result[i - 3]
            result.append(temp)
        return result[-1]

