# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实是找到一个去掉一个元素后，保持数组升序（不可相同）
这里直接罗列规则即可。
"""


class RemoveOneElementToMakeTheArrayStrictlyIncreasing(object):

    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        max_value = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= max_value:
                cnt += 1
                if cnt >= 2:
                    return False
                if i > 1 and nums[i - 2] >= nums[i]:
                    max_value = nums[i - 1]
                else:
                    max_value = nums[i]
            else:
                max_value = nums[i]
        return True


