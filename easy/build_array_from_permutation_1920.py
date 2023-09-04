# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
直接利用Python的数组下标返回重组数据刚好。
"""


class BuildArrayFromPermutation(object):

    def buildArray(self, nums: List[int]) -> List[int]:
        result = list()
        for i in nums:
            result.append(nums[i])
        return result



