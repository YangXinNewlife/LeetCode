# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是将现在的数组变成非递减，
我们可以将：
1.nums[i]降低为num[i + 1]
2.nums[i + 1]升高为[i]
如果可行的话，我们可以将nums[i]降低为num[i + 1]，避免出现我们按照2做调整的时候，nums[i + 1] > nums[i + 2]的情况；
"""


class NondecreasingArray(object):

    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if modified:
                    return False
                if i < 1 or nums[i + 1] > nums[i - 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                modified = True
        return True


