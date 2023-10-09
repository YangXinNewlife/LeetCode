# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
判断是否有连续的三个字符，如果有多出来的话，直接去掉
类似双指针原理
"""


class DeleteCharactersToMakeFancyString(object):

    def makeFancyString(self, s: str) -> str:
        result = list()
        for i in s:
            if len(result) > 1 and result[-1] == i and result[-2] == i:
                continue
            result.append(i)
        return ''.join(result)

