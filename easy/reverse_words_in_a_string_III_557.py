# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解决方法是首先根据空格分割，然后反转每段字符串即可。
"""


class ReverseWordsInAStringIII(object):

    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())



