# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
最长公共重复子串是，该子串的长度一定是str1和str2长度的公因数。
我们只需要找到最小的字符单位，并且递增去判断是否可以满足构成两个串原来的样子。
"""


class GreatestCommonDivisorOfStrings(object):

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_1, len_2 = len(str1), len(str2)
        min_len = min(len_1, len_2)
        result = ""
        for i in range(min_len, 0, -1):
            if len_1 % i or len_2 % i:
                continue
            t1, t2 = len_1 // i, len_2 // i
            gcd = str1[:i]
            new_str1 = gcd * t1
            new_str2 = gcd * t2
            if new_str1 == str1 and new_str2 == str2:
                result = gcd
                break
        return result



