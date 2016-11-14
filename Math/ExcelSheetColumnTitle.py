# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def convertToTitle(self, n):
        res = ''
        while n > 0:
            tmp = n
            n = (tmp - 1)/26
            res += chr(65 + (tmp - 1) % 26)
        return res[::-1]



