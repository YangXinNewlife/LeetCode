# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Solutions:
题目的意思是找出来，有多少个数组对，
(i, j)
nums[i] == nums[j]
i < j
看下有多少对，这里其实就是看每个元素出现的次数，如果出现的次数大于等于2，
则利用个数统计工公式
i * (i - 1) / 2
i是出现的次数
"""


class NumberOfGoodPairs(object):

    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        nums_dict = collections.Counter(nums).values()
        for i in nums_dict:
            if i > 1:
                result += i * (i - 1) / 2
        return int(result)

