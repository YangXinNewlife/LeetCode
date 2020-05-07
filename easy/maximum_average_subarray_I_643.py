# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里题目的意思是计算连续K个子数列中均值等于最大的那组，
因此我们只需要从左到右移动大小为K的窗口，每次计算一次即可，并返回最大值；
"""


class MaximumAverageSubarrayI(object):

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        last_sum = sum(nums[0:k])
        max_sum = last_sum
        for i in range(len(nums) - k):
            last_sum = last_sum + nums[i + k] - nums[i]
            max_sum = max(max_sum, last_sum)
        return max_sum / float(k)


