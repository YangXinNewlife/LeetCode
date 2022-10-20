# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是给出一个数组nums，然后判断数组中，有多少个比自己小的个数，
简单逻辑，打表通过
"""


class HowManyNumbersAreSmallerThanTheCurrentNumber(object):

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = list()
        nums_len = len(nums)
        for i in range(nums_len):
            temp_cnt = 0
            for j in range(nums_len):
                if nums[i] > nums[j]:
                    temp_cnt += 1
            result.append(temp_cnt)
        return result




