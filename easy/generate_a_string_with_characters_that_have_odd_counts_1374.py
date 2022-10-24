# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是给出数字n，返回的字符要求是奇数个，那么其实直接直接可以拆分
n = 奇数 直接 n个'a'
n = 偶数 直接（n - 1）个'a' + 一个'b'
这样无论给出n是什么，都可以保证返回的是奇数个。其中a和b可以换成任意字符。

"""


class GenerateAStringWithCharactersThatHaveOddCounts(object):

    def generateTheString(self, n: int) -> str:
        char_a = 'a'
        char_b = 'b'
        if n % 2 == 1:
            return char_a * n
        else:
            return char_a * (n - 1) + char_b
