# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给定一个数组，然后分别计算
0 ~ i之间的元素的和，直接打表直接AC
"""


class RunningSumOf1dArray(object):

    def runningSum(self, nums: List[int]) -> List[int]:
        result = list()
        for i in range(1, len(nums) + 1):
            result.append(sum(nums[0:i]))
        return result
