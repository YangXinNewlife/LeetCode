# -*- coding:utf-8 -*-
__author__ = 'ryan_yangxin'
"""
Solutions:
题意是找到K个数据中差异最小的，其实拆解起来就是找到两个数据差值最小的值
直接排序然后依次遍历，找到最小值即可。
"""


class MinimumDifferenceBetweenHighestAndLowestOfKScores(object):

    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        result = float("inf")
        for i in range(k - 1, len(nums)):
            result = abs(min(result, abs(nums[i] - nums[i - k + 1])))
        return result

