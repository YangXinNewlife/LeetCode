# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
简单的规则匹配题目；
题意就是说存在两类数，一类是一位的只包含 10 和 11，另一类是 0；
然后我们每次判断给定输入数组长度是 1 的时候，我们只需要返回 True；
如果大于 1位的话，我们每次匹配到 1 的时候，由于只存在 10 和 11 所以跳过 2 位；
否则跳过 1 位，当匹配到最后一位则返回True（说明最后的不是 10 或者 11 组合，我们才能匹配到最后一位，因此正常退出）;
"""


class BitAnd2BitCharacters(object):

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return False



