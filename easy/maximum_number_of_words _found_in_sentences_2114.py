# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
本题读懂应该打表就行
直接判断给定的数组中，最大的元素个数，" "分隔
"""


class MaximumNumberOfWordsFoundInSentences(object):

    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for i in sentences:
            result = max(result, len(str(i).split(" ")))
        return result
