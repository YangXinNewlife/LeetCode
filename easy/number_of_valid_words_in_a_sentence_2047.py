# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是找到给定的字符串sentence是否符合规定，
多是小写字符，不含非-的符号，如果包含的话要在中间。
再通过递归判断即可
"""


class NumberfValidWordsInASentence(object):

    def countValidWords(self, sentence: str) -> int:
        return sum(self.is_valid(k) for k in sentence.split())

    def is_valid(self, str):
        temp_result = False
        for i, j in enumerate(str):
            if j.isdigit() or j in '!.,' and i < len(str) - 1:
                return False
            if j == '-':
                if temp_result or i == 0 or i == len(str) - 1 or not str[i - 1].islower() or not str[i + 1].islower():
                    return False
                temp_result = True
        return True

