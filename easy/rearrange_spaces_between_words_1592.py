# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
题意是将所有的空格按照规则平均分配到字符中
规则1：只有一个字符串时，则把所有的空格都放到最后
规则2：如果是多个字符串时，先将空格除以字符串个数，
平均分在字符串中，剩余空格放在后面即可
"""


class RearrangeSpacesBetweenWords(object):

    def reorderSpaces(self, text: str) -> str:
        space_cnt = text.count(' ')
        word_list = text.strip().split()
        text_len = len(word_list)
        if text_len == 1:
            return ' '.join(word_list) + ' ' * space_cnt
        mid_space = space_cnt // (text_len - 1)
        other_space = space_cnt % (text_len - 1)
        return (' ' * mid_space).join(word_list) + ' ' * other_space




