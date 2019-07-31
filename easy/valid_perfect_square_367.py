# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
这里使用的思路是二分搜索
左右各一个指针
"""


class ValidPerfectSquare(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left <= right:
            mid = (left + right) / 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


