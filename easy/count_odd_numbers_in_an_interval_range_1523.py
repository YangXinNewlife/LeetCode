# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
统计区间内奇数的个数，直接使用计数公式即可，我们在判断下，是否末尾和首位都为奇数，
是的话再加1刚好，否则就直接个数除以2求整。
"""


class CountOddNumbersInAnIntervalRange(object):

    def countOdds(self, low: int, high: int) -> int:
        cnt = high - low + 1
        if low % 2 == 1 and high % 2 == 1:
            return cnt // 2 + 1
        return cnt // 2

