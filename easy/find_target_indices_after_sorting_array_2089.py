# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是指我们将数组排序后，查找给定的目标值target在数组中的下标
这里直接模拟查找即可
"""


class FindTargetIndicesAfterSortingArray(object):

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = list()
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result
