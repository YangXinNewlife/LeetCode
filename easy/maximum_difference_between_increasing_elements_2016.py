# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是找出来升序最大的差值，
直接遍历即可。
"""


class MaximumDifferenceBetweenIncreasingElements(object):

    def maximumDifference(self, nums: List[int]) -> int:
        result_list = list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                result_list.append(nums[j] - nums[i])
        max_value = max(result_list)
        if max_value <= 0:
            return -1
        else:
            return max_value
