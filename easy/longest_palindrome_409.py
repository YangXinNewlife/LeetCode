# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Solutions:
统计最大的组合回文，这里可以使用统计字母的方法，
例如：
    1.若字母出现偶数次，则直接累加值最终结果
    2.若字母出现奇数次，则-1后再累加值最终结果
"""


class LongestPalindrome(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = collections.Counter(s)
        sum = 0
        for item in dict:
            number = dict[item]
            double = number if number % 2 == 0 else number - 1
            dict[item] -= double
            sum += double
        print(dict)
        if 1 in dict.values():
            sum += 1
        return sum



