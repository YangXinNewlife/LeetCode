# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是给出一个数组，
例子：[1,2,3,4]
我们读区频率和数值变量
频率：1
数值：2
--------
频率：3
数值：4
因此按照频率生成数组就是
[2]、[4,4,4]
"""


class DecompressRunLengthEncodedList(object):

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = list()
        for i in range(len(nums)):
            if i % 2 == 1:
                for j in range(nums[i - 1]):
                    result.append(nums[i])
        return result
