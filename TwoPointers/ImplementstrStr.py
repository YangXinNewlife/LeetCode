# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def strStr(self, haystack, needle):
        start= 0
        while start <= (len(haystack) - len(needle)):
            i1 = start
            i2 = 0
            while (i2 < len(needle) and haystack[i1] == needle[i2]):
                i1 += 1
                i2 += 1

            if i2 == len(needle):
                return start
            start += 1
        return -1