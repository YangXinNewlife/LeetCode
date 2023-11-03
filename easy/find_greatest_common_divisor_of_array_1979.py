# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
找到最大公约数
直接打表处理，第一轮先判断是否可以
max_num % min_num == 0:
不行的话，遍历最小的数到1，找到公约数即可
"""


class FindGreatestCommonDivisorOfArray(object):

    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        if max_num % min_num == 0:
            return min_num
        for j in range(min_num, 0, -1):
            if max_num % j == 0 and min_num % j == 0:
                return j



