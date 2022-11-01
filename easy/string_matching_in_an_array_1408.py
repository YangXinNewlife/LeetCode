# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是判断给出的字符串组中哪些是其他的子串
由于子串不得不考虑到长度的问题，短的可能是长的子串，
因此直接循环比例即可。
"""


class StringMatchingInAnArray(object):

    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        words.sort(key=len)
        words_len = len(words)
        for i in range(words_len):
            for j in range(i + 1, words_len):
                if words[i] in words[j]:
                    result.add(words[i])
        return result



