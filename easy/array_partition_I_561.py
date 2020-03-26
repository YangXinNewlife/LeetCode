# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions：我们先理解题目的意思，其实是输入2n个数字，然后分成n对（分区），
分区的方式要求累加其中每对的min()值，
因此我们想到就是尽可能吧每个值都按照升序的方式排序，然后然后计算出来的和就好了。
"""


class ArrayPartitionI(object):

    def arrayPairSum(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        """
        sum_result = 0
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                sum_result += nums[i]
        return sum_result






