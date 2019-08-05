# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Soltions:
这里使用集合的方式来查询对应的数据量的大小以及key的差异。
"""


class FindTheDifference(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        return (dt - ds).keys().pop()
