# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是在给定的字符串中，可以找到多少可以分割的对称字符串。
我们设计两个计数器即可。
l_cnt计数器，计算L的个数；
r_cnt计数器，计算R的个数；
当L = R的时候说明出现了一对，
最后统计多少对即可。
"""

class SplitAStringInBalancedStrings(object):

    def balancedStringSplit(self, s: str) -> int:
        l_cnt = r_cnt = result_cnt = 0
        for i in s:
            if i == 'R':
                r_cnt += 1
            elif i == 'L':
                l_cnt += 1
            if l_cnt != 0 and r_cnt != 0 and l_cnt == r_cnt:
                result_cnt += 1
                l_cnt = r_cnt = 0
        return result_cnt

