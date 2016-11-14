# -*- coding:utf-8 --
__author__ = 'jiuzhang'
class Solution(object):
    def integerReplacement(self, n):
        if n == 1:
            return 0
        if n % 2 == 0:
            return (1 + self.integerReplacement(n/2))
        else:
            return 2 + min(self.integerReplacement((n + 1)/2), self.integerReplacement((n - 1)/2))




