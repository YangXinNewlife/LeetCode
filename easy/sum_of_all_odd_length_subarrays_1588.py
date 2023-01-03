# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是计算奇数个子序列的所有元素的和
首选要计算出来我们要计算奇数的长度有多少。
for i in range(1, (len(arr) + 1), 2)
然后分别计算对应 i 个的元素值
arr[j:j + i]
"""


class SumOfAllOddLengthSubarrays(object):

    def sumOddLengthSubarrays(self, arr) -> int:
        result = 0
        for i in range(1, (len(arr) + 1), 2):
            for j in range(len(arr) - i + 1):
                result += sum(arr[j:j + i])
        return result
