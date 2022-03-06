# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是找出来提示的单词first和second后面的单词，可能出现多个。
方法就是遍历比对即可
"""


class OccurrencesAfterBigram(object):

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = list()
        text_list = text.split(" ")
        text_len = len(text_list)
        for i in range(text_len - 2):
            if text_list[i] == first and text_list[i + 1] == second:
                result.append(text_list[i + 2])
        return result

