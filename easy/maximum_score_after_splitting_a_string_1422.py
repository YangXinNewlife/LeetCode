# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是将给定的字符串s，按照顺序做切分，然后分别统计切分后左侧的0的个数和右侧1的个数。
求出左侧和右侧个数求和的最大和（分值）是多少。
左右最少要保留一个，因此，我们保留右侧最少一个。
for i in range(len(s) - 1)
"""


class MaximumScoreAfterSplittingAString(object):

    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(len(s) - 1):
            zero_cnt = s[0: i + 1].count('0')
            one_cnt = s[i + 1:].count('1')
            max_score = max(max_score, zero_cnt + one_cnt)
        return max_score

