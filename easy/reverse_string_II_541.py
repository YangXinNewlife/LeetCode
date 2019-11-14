# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions：
这道题目只要理解了题意基本上可以操作，
我这里的判断字符串的长度，然后进行反转即可。
"""


class ReverseStringII(object):

    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for i in range(0, len(s_list), 2 * k):
            s_list[i: i + k] = reversed(s_list[i: i + k])
        return "".join(s_list)


