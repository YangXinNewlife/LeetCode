# -*- coind:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给定数组nums，然后一个最短距离k，
然后遍历数组看下是否有两个1之间的距离小于给定的最小限定k，有的话返回False
否则返回True
"""


class CheckIfAll1sAreAtLeastLengthKPlacesAway(object):

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if sum(nums) <= 1 or sum(nums) == len(nums):
            return True
        lst_one = nums.index(1)
        for i in range(lst_one + 1, len(nums)):
            if nums[i] == 1 and i - lst_one - 1 < k:
                return False
            elif nums[i] == 1:
                lst_one = i
        return True


