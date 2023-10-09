# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实几句是判断给定的字符串改成数组，
然后判断每个元素是否出现在坏掉的按键中，
如果有存在坏掉则不能打出来，
所以直接break即可，最后判断能打印出几个就行
"""


class MaximumNumberOfWordsYouCanType(object):

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_list = text.split(" ")
        result = len(text_list)
        for i in text_list:
            for j in i:
                if j in brokenLetters:
                    result -= 1
                    break
        return result
