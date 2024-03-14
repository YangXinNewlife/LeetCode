# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题目的意思就是对每个元素的位置进行除以10，求余数是否和当前元素一致，因为是已经排序的，
所以直接判断即可，遇到就返回就可以。
"""


class SmallestIndexWithEqualValue:

    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

