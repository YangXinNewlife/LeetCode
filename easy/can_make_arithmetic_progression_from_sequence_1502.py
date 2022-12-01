# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是计算重排后的字符串是否是等差数列，
返回是或否即可。
"""


class CanMakeArithmeticProgressionFromSequence(object):

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        if len(arr) == 2:
            return True
        else:
            diff = abs(arr[0] - arr[1])
        for i in range(2, len(arr)):
            if abs(arr[i] - arr[i - 1]) != diff:
                return False
        return True

