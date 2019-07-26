# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
1.先计算最大值到最小值的和;
2.再计算输入数据的和;
3.再计算两个和的差，就是缺少的值;
"""


class MissingNumber(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = len(nums) * (len(nums) + 1) / 2
        sum_total = sum(nums)
        return temp_sum - sum_total


