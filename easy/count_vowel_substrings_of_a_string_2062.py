# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实是判断给出的字符串包含多少个含有aeiou元素的子串
这里直接先预定一个set包含aeiou
然后直接判断字符串，没加一个判断是否和之前保持一致。
"""


class CountVowelSubstringsOfAString(object):

    def countVowelSubstrings(self, word: str) -> int:
        result_set = set()
        result_set.add('a')
        result_set.add('e')
        result_set.add('i')
        result_set.add('o')
        result_set.add('u')
        result = 0
        word_len = len(word)
        for i in range(word_len):
            temp_set = set()
            for j in range(i, word_len):
                temp_set.add(word[j])
                if result_set == temp_set:
                    result += 1
        return result




