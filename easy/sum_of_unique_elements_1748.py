# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是计算给定的数组中唯一元素的和，
直接使用哈希的算法原理，先初始化出
[0] * (max(nums) + 1)个大小的数组元素
然后利用哈希操作
最后判断是否等于1即可。
"""


class SumOfUniqueElements(object):

    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        temp_result = [0] * (max(nums) + 1)
        for i in nums:
            temp_result[i] += 1
        for j in range(len(temp_result)):
            if temp_result[j] == 1:
                result += j
        return result

