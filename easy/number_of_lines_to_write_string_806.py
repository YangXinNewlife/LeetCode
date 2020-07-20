# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定每个字符的元素占用大小，以及给定对应的元素；
还给定每行最大100，那么我们只需要依次遍历每个元素找到对应的大小，判断大于100时，直接换行即可；
"""


class NumberOfLinesToWriteString(object):

    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        width = 0
        line = 1
        for i in S:
            width += widths[ord(i) - ord('a')]
            if width > 100:
                width = widths[ord(i) - ord('a')]
                line += 1
        return line, width
