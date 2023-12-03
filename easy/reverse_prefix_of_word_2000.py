# -*- coding:utf-8 -*-
__author__ = 'ryan_yangxin'
"""
Solutions:
该问题其实是反转字符串，
这里是区间反转
利用ch定位下标即可
"""


class ReversePrefixOfWord(object):

    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            for i in range(len(word)):
                if word[i] == ch:
                    return word[i::-1] + word[i + 1:]

