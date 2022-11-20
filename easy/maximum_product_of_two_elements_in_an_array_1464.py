# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
打表的题目，就是判断两个数通过-1后相乘最大。
"""


class MaximumProductOfTwoElementsInAnArray(object):

    def maxProduct(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                result = max(result, (nums[i - 1] - 1) * (nums[j] - 1))
        return result

