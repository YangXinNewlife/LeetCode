# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数组，然后找出来某一个值（可以不在数组中）。
依次和数组中元素求和，寻找出来求和都大于等于1那个值。
因此我们可以遍历每个值的求和，找出来最小的那个，然后 + 1，
即可得到所有都大于1的求和。
"""


class MinimumValueToGetPositiveStepByStepSum(object):

    def minStartValue(self, nums: List[int]) -> int:
        result = 0
        tmp = 0
        for i in range(len(nums)):
            tmp = tmp + nums[i]
            result = min(result, tmp)
        if result < 0:
            result = abs(result)
        return result + 1


