# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：题意是将现在的数组变成非递减，
我们这里定一个判断是否为非递减数列的lambda函数，
因为会出现两种情况，第一种调整前者 i,第二种调整后者 i + 1。
为此我们可以分别处理最后选一种可行的解，
即
is_increase(first_nums) or is_increase(copy_nums)
"""


class NondecreasingArray(object):

    def checkPossibility(self, nums: List[int]) -> bool:
        is_increase = lambda nums: all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
        first_nums, copy_nums = nums[:], nums[:]
        for i in range(0, len(nums) - 1):
            if nums[i + 1] < nums[i]:
                first_nums[i] = first_nums[i + 1]
                copy_nums[i + 1] = copy_nums[i]
                break
        return is_increase(first_nums) or is_increase(copy_nums)


