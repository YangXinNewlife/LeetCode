# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义就是在给定的数组中能否找到最大的一个元素，比第二大的元素还要大，如果是的话，返回这个最大的元素下标，否则的话返回 -1，
按照题目的意思整理处理就好了。
"""


class LargestNumberAtLeastTwiceOfOthers(object):

    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums_temp = nums[:]
        nums.sort()
        if nums[-1] >= nums[-2] * 2:
            return nums_temp.index(nums[-1])
        else:
            return -1


