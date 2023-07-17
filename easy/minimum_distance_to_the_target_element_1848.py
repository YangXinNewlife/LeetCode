# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是基于给定的数组，找出来一个最小的值，
其中需要符合
nums[i] == target 且在符合当中，
abs(i-start)最小的，因此直接遍历套用公式即可。
"""


class MinimumDistanceToTheTargetElement(object):

    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = list()
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(abs(i-start))
        return min(result)

