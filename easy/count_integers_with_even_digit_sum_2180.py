# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意是给定一个数字num，需要统计下小于等于num的数字符合每个元素求和是偶数的。
"""

class CountIntegersWithEvenDigitSum(object):

    def countEven(self, num: int) -> int:
        result = 0
        for i in range(1, num + 1):
            num_sum = 0
            for j in range(len(str(i))):
                num_sum += int(str(i)[j])
            if num_sum % 2 == 0:
                result += 1
        return result

