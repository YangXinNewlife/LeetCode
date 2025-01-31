# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意是给定一组数组，其中如果元素相同的情况下，下标还可以相乘且可以被K除情况下，统计有多少组。
这里直接打表完成计算。
"""

class CountEqualAndDivisiblePairsInAnArray(object):

    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    result += 1
        return result
