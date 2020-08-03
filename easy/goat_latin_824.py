# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
其实这道题目只要看懂题意就可以做得出来，这里可以看到分三种情况处理：
1.如果单词以元音字母开头，后面接上"ma"；
2.如果不以元音开头，把首字母移到最后，然后接上"ma"；
3.每个单词后面接上，当前单词在句子中出现的几位置（从1开始）乘以 "a"，第一个单词的话就是"a", 第二个就是"aa"...
"""


class GoatLatin(object):

    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split(" ")
        temp_words = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word += 'a' * (i + 1)
            temp_words.append(word)
        return " ".join(temp_words)

