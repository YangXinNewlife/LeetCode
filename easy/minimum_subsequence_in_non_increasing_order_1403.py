# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是：
给定数组nums，获得数组的一个子序列sublist，该子序列的元素之和严格大于该子序列中未包含元素的总和。
如果存在多个解，则返回具有最小大小的子序列；如果仍然存在多个解决方案，则返回其所有元素的最大总和的子序列。
阵列的子序列可以通过从阵列中删除一些（可能为零）元素来获得。
请注意，具有给定约束的解决方案保证是唯一的。同时返回按非递增顺序排序的答案。
规则看起来很复杂，其实我们可以先排序，
然后依次出栈，不断求和即可。
"""


class MinimumSubsequenceInNonIncreasingOrder(object):

    def minSubsequence(self, nums: List[int]) -> List[int]:
        result = list()
        nums.sort()
        while sum(result) <= sum(nums):
            result.append(nums.pop())
        return result

