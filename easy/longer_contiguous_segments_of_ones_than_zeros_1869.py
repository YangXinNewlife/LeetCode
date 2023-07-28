# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义判断出来最长的连续字符串1是否比0的多？
直接基于0和1统计下即可
"""


class LongerContiguousSegmentsOfOnesthanZeros(object):

    def checkZeroOnes(self, s: str) -> bool:
        elem_1_list = s.split("0")
        max_1_len = max([len(i) for i in elem_1_list])
        elem_0_list = s.split("1")
        max_0_len = max([len(i) for i in elem_0_list])
        return max_1_len > max_0_len


