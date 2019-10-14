# -*- coidng:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题思路是看懂题意就很好解决，
题目的意思是根据输入的字符串，筛选出来哪些字符串都在同一行中，存在的话，返回字符串。
"""


class KeyboardRow(object):

    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        output = []
        for i in words:
            for j in keyboard:
                lword = i.lower()
                if set(lword).issubset(set(j)):
                    output.append(i)
        return output

