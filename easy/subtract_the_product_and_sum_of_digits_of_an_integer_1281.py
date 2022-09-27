# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是计算"求和"、"乘法"两个数的差值
就是按照正常的按位除法计算即可
"""


class SubtractTheProductAndSumOfDigitsOfAnInteger(object):

    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        while n > 0:
            x = n % 10
            prod *= x
            sum += x
            n //= 10
        return prod - sum

