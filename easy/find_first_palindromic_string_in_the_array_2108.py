# -*- code:utf-8 -*-
__author__ = 'yangxin_ryan'

"""
Solution:
题意是找出来给定的字符数组中，第一个回文字符串。
我们直接遍历每个元素，取反即可。判断当前元素和取反是否一致。
"""


class FindFirstPalindromicStringInTheArray(object):

    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ''
