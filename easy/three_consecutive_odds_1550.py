# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是判断给定的数组中，是否有满足三个连续的奇数，不满足返回False，否则返回True
通过累加计数器的方式计算即可。
"""


class ThreeConsecutiveOdds(object):

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for i in arr:
            if i % 2 == 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False




