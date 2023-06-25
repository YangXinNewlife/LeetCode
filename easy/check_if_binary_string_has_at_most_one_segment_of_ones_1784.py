# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是基于给定的s字符串
需要判断下是否有长度连续大于1的连续的1，
有的话范围False, 否则返回True
"""


class CheckIfBinaryStringHasAtMostOneSegmentOfOnes(object):

    def checkOnesSegment(self, s: str) -> bool:
        ones_list = s.split("0")
        cnt = 0
        for i in ones_list:
            if len(i) > 0:
                cnt += 1
                if cnt > 1:
                    return False
        return True

