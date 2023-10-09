# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意说的是给定字符串s包含小写字符和数字。经过k次转换，求计算后的结果。
直接通过ord()函数进行计算，但是需要两次计算逻辑，
第一个逻辑是先转译，后计算。
"""


class SumOfDigitOfStringAfterConvert(object):

    def getLucky(self, s: str, k: int) -> int:
        result = 0
        for i in s:
            temp = ord(i) - 96
            result += temp % 10 + temp // 10

        for j in range(k - 1):
            temp = result
            result = 0
            while temp:
                result += temp % 10
                temp //= 10
        return result
