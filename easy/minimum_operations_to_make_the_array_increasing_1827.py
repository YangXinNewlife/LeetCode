# -*- coding:utf-8 -*-
__authir__ = 'yangxin_ryan'
"""
Solutions:
题意是将原有的数组nums经过最小的操作，处理为递增（元素间隔为1的）数组。
简单操作就是从第二个元素开始，
因此只需要用元素和last_value判断即可。
last_value + 1 - i可以得出需要操作几次。
"""


class MinimumOperationsToMakeTheArrayIncreasing(object):

    def minOperations(self, nums: List[int]) -> int:
        last_value = nums[0]
        result = 0
        for i in nums[1:]:
            if i < last_value + 1:
                result += last_value + 1 - i
                last_value += 1
            else:
                last_value = i
        return result

























