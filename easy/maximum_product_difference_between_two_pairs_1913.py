# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目要求找到两个Paird的差异
计算公式为：
最大的 * 第二大的 - 最小的 * 第二小的
这里直接排序操作即可。
"""


class MaximumProductDifferenceBetweenTwoPairs(object):

    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return nums[0] * nums[1] - nums[-1] * nums[-2]
