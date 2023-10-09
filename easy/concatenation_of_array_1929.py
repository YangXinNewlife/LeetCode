# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
参考demo:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
直接打表循环赋值即可。
result[i] = nums[i]
result[i + len_num] = nums[i]
"""


class ConcatenationOfArray(object):

    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_num = len(nums)
        result = list([0] * len_num * 2)
        for i in range(len_num):
            result[i] = nums[i]
            result[i + len_num] = nums[i]
        return result





