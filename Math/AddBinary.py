# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(str(int(a, 2) + int(b, 2))))[2:]
