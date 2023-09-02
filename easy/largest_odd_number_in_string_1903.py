# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是找到字符串中的最大奇数，
方案是从字符串最后一个元素往前找，只要是奇数直接返回即可。
"""


class LargestOddNumberInString(object):

    def largestOddNumber(self, num: str) -> str:
        num_len = len(num)
        while num_len > 0 and int(num[n - 1]) % 2 == 0:
            num_len -= 1
        return num[:num_len]

