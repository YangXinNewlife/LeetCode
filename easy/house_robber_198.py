# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
我们分别用两个变量，我们采用动态规划DP 
公式为max(i + temp, result)
temp 保存上一次计算的最大值
result = 保存最终的最大值
计算推演：
测试数据 [2, 7, 9, 3, 1]

i = 2
temp = 0
result = max(2 + 0, 0) = 2
----------- 到目前为止最大的保存在result中为 2

i = 7
temp = 2
result = max(7 + 0, 2)
----------- 到目前为止最大的保存在result中为 7

i = 9
temp = 7
result = max(9 + 2, 7) = 11
------------ 到目前为止最大的保存在result中为 11

i = 3
temp = 11
result = max(3 + 7, 11) = 11
------------- 到目前为止最大的保存在result中为 11

i = 1
temp = 11
result = max(1 + 11, 11) = 12
-------------- 到目前为止最大的保存在result中为 12
"""


class HourseRobber(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, temp = 0, 0
        for i in nums:
            temp, result = result, max(i + temp, result)
        return result

