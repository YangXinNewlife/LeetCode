# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
逻辑就是判断一共需要转换几次，才可以将元素X都转换为0，
每次转换最多3个因此只需要每次转换的第一个元素是否是X，
是的话，直接下标+3，否则跳过。
"""


class MinimumMovesToConvertString(object):

    def minimumMoves(self, s: str) -> int:
        result = 0
        index = 0
        for i, j in enumerate(s):
            if i >= index and j == 'X':
                result += 1
                index = i + 3
        return result

