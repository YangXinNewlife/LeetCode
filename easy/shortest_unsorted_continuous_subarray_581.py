# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是在一个数组中找出来最短的不用排序的子数组长度。
解决办法可以使用排序的方式，然后去对比数组中的元素，然后不相同的首尾部分长度记为该数组的长度；
"""


class ShortestUnsortedContinuousSubarray(object):

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = [i for i in nums]
        nums.sort()
        min_index = 0
        max_index = 0
        flag = 0
        for i in range(len(nums)):
            if nums[i] == nums_copy[i]:
                continue
            else:
                flag = 1
                min_index = i
                break
        if flag == 0:
            return 0
        for i in range(len(nums)):
            if nums[-i-1] == nums_copy[-i-1]:
                continue
            else:
                max_index = -i
                break
        return len(nums) + max_index - min_index
