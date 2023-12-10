# -*- coding:utf-8 -*-
__author__ = 'ryan_yangxin'
"""
Solutions:
基于题目两个元素的差值绝对值等于K即可，统计符合的数量。
"""


class CountNumberOfPairsWithAbsoluteDifferenceK(object):

    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0
        nums_len = len(nums)
        for i in range(0, nums_len):
            for j in range(i + 1, nums_len):
                if abs(nums[i] - nums[j]) == k:
                    result += 1
        return result
