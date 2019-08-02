# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里使用Hash的思想去统计每个字符出现的次数，
然后我们通过判断第一个出现（第一个次数为1）的字符为返回的结果。
"""


class FirstUniqueCharacterInAString(object):

    def firstUniqChar(self, s):
        """
        hash的思想
        :type s: str
        :rtype: int
        """
        char_list = [0] * 26
        for i in s:
            char_list[ord(i) - 97] += 1
        for j, k in enumerate(s):
            if char_list[ord(k) - 97] == 1:
                return j
        return -1


