# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions
解题思路是首先我们用一个set的去重来处理重复的morse数据，然后依次遍历每个元素，
然后每一个字符，将对应的元素的字符morse做拼接，存储到去重的结合中即可；
最后返回个数；
"""


class UniqueMorseCodeWords(object):

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_set = set()
        for i in words:
            temp_morse = ''
            for j in i:
                temp_morse += morse[ord(j) - ord('a')]
            morse_set.add(temp_morse)
        return len(morse_set)



