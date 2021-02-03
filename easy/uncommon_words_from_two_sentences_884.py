# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是我们找出来两个字符串中单个单词是什么，如果出现了两次也不算单个，如下例子；
A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Input: A = "apple apple", B = "banana"
Output: ["banana"]

那么这种很明显的去重我们可以使用SET可完成
"""


class UncommonWordsFromTwoSentences(object):

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a_list = A.split(" ")
        b_list = B.split(" ")
        a_count, b_count = collections.Counter(a_list), collections.Counter(b_list)
        a_set = {key for key, count in a_count.items() if count == 1}
        b_set = {key for key, count in b_count.items() if count == 1}
        ab_set = set(a_list) & set(b_list)
        return list({x for x in a_set^b_set if x not in ab_set})


