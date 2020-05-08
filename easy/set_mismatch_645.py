# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给出一个包含重复元素的由1到n的列表，
要我们返回一个数组,共两个元素，第一个元素是重复的数据，第二个是缺失的数据，
1.怎么寻找重复的数据：计算nums的总和-去重后的总和；
1.怎么寻找缺失的数据：我们使用 n*(n+1)/2 来计算正常逻辑下1～n的总和，然后和去重后的总和做减法，就可以求出缺失的数据； 
"""


class SetMismatch(object):

    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_distinct_nums = sum(set(nums))
        return [sum(nums) - sum_distinct_nums, int(n * (n + 1) / 2 - sum_distinct_nums)]
