# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目就是给定数字个数n,
然后依次累加
1 ...7
2 ...8
3 ...9
n
模拟求和即可，就判断是否整除即可
"""


class CalculateMoneyInLeetcodeBank(object):

    def totalMoney(self, n: int) -> int:
        result = 0
        cnt = 1
        for i in range(1, n + 1):
            if i % 7:
                result += (cnt - 1) + i % 7
            else:
                result += cnt + (i - 1) % 7
                cnt += 1
        return result
