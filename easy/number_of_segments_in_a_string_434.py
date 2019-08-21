# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
返回字符串统计，我们只需要根据空格做分割即可。
"""


class NumberOfSegmentsInAString(object):

    def countSegments(self, s: str) -> int:
        """
        :param s:
        :return:
        """
        return len(s.split())
