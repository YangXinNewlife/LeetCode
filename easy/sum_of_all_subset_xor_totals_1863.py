# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实是要多所有的元素排列组合中
进行异或运算^=
那么直接遍历
对于排列组合使用itertools.combinations即可
"""
import itertools


class SumOfAllSubsetXORTotals(object):

    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums) + 1):
            for j in itertools.combinations(nums, i):
                temp = 0
                for k in j:
                    temp ^= k
                result += temp
        return result



