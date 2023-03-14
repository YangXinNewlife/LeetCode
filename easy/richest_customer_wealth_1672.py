# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意是统计每个子数组的元素和，找出最大值即可。
"""


class RichestCustomerWealth(object):

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


