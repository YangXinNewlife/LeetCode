# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def findNthDigit(self, n):
        if n < 0:
            return 0
        count = 9
        start = 1
        length = 1
        while n > (length * count):
            n -= length * count
            length += 1
            start *= 10
            count *= 10
        start += (n - 1)/length
        return int((str(start)[(n - 1)%length]))





