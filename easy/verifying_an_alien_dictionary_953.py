# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目含义的意思就是对于给定字符串数据中的相同位置字符，是不是按照给定order字典排序的方式，
顺序正确返回True，否则返回False。
"""


class VerifyingAnAlienDictionary(object):

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        length = len(words)
        for i in range(length - 1):
            pre = words[i]
            after = words[i + 1]
            min_len = min(len(pre), len(after))
            for j in range(min_len):
                if order.index(pre[j]) < order.index(after[j]):
                    break
                elif order.index(pre[j]) > order.index(after[j]):
                    return False
                elif j == min_len - 1 and len(after) < len(pre):
                    return False
        return True



