# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定两个数字，如果两个数字都大于0的话，都需要进行减法（大的减去小的），然后再进行比较依次反复。
最后出现有一个小于等于0，就结束计算，最后只需要统计出一共计算了多少次即可。
直接模拟打表操作。
"""

class CountOperationsToObtainZero(object):

    def countOperations(self, num1: int, num2: int) -> int:
        result = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 = num1 - num2
            elif num2 > num1:
                num2 = num2 - num1
            result += 1
        return result
