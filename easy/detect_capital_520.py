# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
直接使用python字符串自带的函数来处理
* .isupper()是否都是大写
* .islower()是否都是小写
* .istitle()是否是大写开头
"""


class DetectCapital(object):

    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.istitle() or word.islower()

