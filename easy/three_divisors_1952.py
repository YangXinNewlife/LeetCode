# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数字n，判断n有几个因子整除即可，遍历打表处理即可。
"""


class ThreeDivisors(object):

    def isThree(self, n: int) -> bool:
        result = 0
        for i in range(1, n + 1):
            if n % i == 0:
                result += 1
        return result == 3




