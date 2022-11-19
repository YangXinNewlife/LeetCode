# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给定一个字符串（由一个空格分隔），然后判断下给定的searchWord
是否是每一个子字符串的前缀
"""


class CheckIfAWordOccursAsAPrefixOfAnyWordInASentence(object):

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        result = -1
        str_list = sentence.split(" ")
        list_size = len(str_list)
        for i in range(list_size):
            if str(str_list[i]).startswith(searchWord):
                result = i + 1
                break
        return result
