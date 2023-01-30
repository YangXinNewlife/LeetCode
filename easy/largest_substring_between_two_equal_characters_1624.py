# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是返回两个相同字符之间的距离差，
处理逻辑其实就是遍历字符串中的每个元素，
并用字典的方式记录每个元素的位置，然后如果出现第二次的话，
就用result保存下当前连个相同元素之间的距离差，用max记录下最大的，
直到遍历完成。

"""


class LargestSubstringBetweenTwoEqualCharacters(object):

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        len_dict = dict()
        result = -1
        for i in range(len(s)):
            if s[i] in len_dict.keys():
                result = max(result, i - len_dict[s[i]] - 1)
            else:
                len_dict[s[i]] = i
        return result



