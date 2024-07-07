# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意是给定一个数组，我们要找到其中连续的最大K个元素子串的和。
我们可以先利用对元素的排序，获取数组下标的顺序。
然后判断这些最大下标的元素，返回下标顺序的元素集合。
"""


class FindSubsequenceOfLengthKWithTheLargestSum(object):

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        result = list()
        n = len(nums)
        nums_sorted = sorted(range(n), key=lambda i: -nums[i])
        for j in range(n):
            if j in set(nums_sorted[:k]):
                result.append(nums[j])
        return result


