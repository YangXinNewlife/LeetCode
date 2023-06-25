# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是判断两个字符串s1和s2,
如果将s1或者s2字符串中的两个元素交换可以等于另一个字符串
返回True，否则返回False，
直接规则判即可
"""
import collections


class CheckIfOneStringSwapCanMakeStringsEqual(object):

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        s1_counter = collections.Counter(s1)
        s2_counter = collections.Counter(s2)
        if s1_counter != s2_counter:
            return False
        cnt = 0
        for i in range(len(s1)):

            if s1[i] != s2[i]:
                cnt += 1
                if cnt >= 3:
                    return False
        return True
