# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是找出来连续升序的最长子串的和，
这里找一个临时的计数器temp_result，
然后遍历时判断下是否当前的元素大于前一个，
大于则累计
小于则重新累计
"""


class MaximumAscendingSubarraySum(object):

    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        temp_result = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp_result += nums[i]
                result = max(result, temp_result)
            else:
                temp_result = nums[i]
        return result



