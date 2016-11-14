# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def titleToNumber(self, s):
        res = 0
        for i in range(len(s)):
            res = res * 26 + (ord(s[i]) - ord('A') + 1)
        return res
