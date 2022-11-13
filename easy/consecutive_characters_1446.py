# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个字符串s，找出字符串中连续相同的子串中，最长的个数。
打表直接遍历判断即可.
"""


class ConsecutiveCharacters(object):

    def maxPower(self, s: str) -> int:
        result = 1
        temp_cnt = 1
        pre_char = s[0]
        for i in range(1, len(s)):
            if pre_char == s[i]:
                temp_cnt += 1
            else:
                temp_cnt = 1
                pre_char = s[i]
            result = max(result, temp_cnt)
        return result




