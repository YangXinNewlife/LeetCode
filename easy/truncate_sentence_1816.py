# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
直接基于空格切分并返回对应个字符串即可
"""


class TruncateSentence(object):

    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])

