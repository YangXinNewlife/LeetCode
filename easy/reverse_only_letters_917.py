# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是反转给定字符串的每个字符（但是不包括符号），我们想到的可以使用数组模拟栈的结构来操作，
先筛选出来所有的字母放到letters中，然后顺序便利字符串，遇到字母时出栈，不是字母返回符号即可；
"""


class ReverseOnlyLetters(object):

    def reverseOnlyLetters(self, S: str) -> str:
        letters = list()
        result = ""
        for i in S:
            if i.isalpha():
                letters.append(i)
        for j in S:
            if j.isalpha():
                result += letters.pop()
            else:
                result += j
        return result


