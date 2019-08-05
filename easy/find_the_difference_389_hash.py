# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solotions:
这里使用hash算法，
利用标记数据差寻找对应新增的数据。
"""


class FindTheDifference(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_list = [0] * 26
        for i in s:
            hash_list[ord(i) - 97] += 1
        for j in t:
            hash_list[ord(j) - 97] -= 1
            if hash_list[ord(j) - 97] < 0:
                return j
