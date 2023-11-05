# -*- coding:utf-8 -*-
__author__ = 'ryan_yangxin'
"""
Solutions:
题意说的是找出来数组中的一个元素i，
符合定义，该元素i的左右两侧的和刚好相同
那么直接套用公式即可。
"""


class FindTheMiddleIndexInArray(object):

    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        temp_sum = 0
        for i in range(len(nums)):
            if temp_sum * 2 == total_sum - nums[i]:
                return i
            temp_sum += nums[i]
        return -1
