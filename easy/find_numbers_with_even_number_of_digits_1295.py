# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是判断每个数值的个数是偶数的
直接通过长度判断即可
len(str(i)) % 2 == 0
"""


class FindNumbersWithEvenNumberOfDigits(object):

    def findNumbers(self, nums: List[int]) -> int:
        result_list = list()
        for i in nums:
            if len(str(i)) % 2 == 0:
                result_list.append(i)
        result = len(result_list)
        return result
