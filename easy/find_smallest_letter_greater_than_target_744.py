# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意理解了基本就能做出来，首先给出一个有序的字符数组letters，然后给定一个target字符，
要我们找到数组中第一个比这个字符大的字符，如果没有的话，返回letters中的第一个字符；
"""


class FindSmallestLetterGreaterThanTarget(object):

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = letters[0]
        for i in letters:
            if i > target:
                result = i
                break
        return result
