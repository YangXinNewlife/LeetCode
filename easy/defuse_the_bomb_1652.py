# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是基于给定的code数组，和k，
基于k的数值做不同的处理
k = 0, 则返回全部长度的0。
k > 0, 则返回前K个数值的和。
k < 0, 则返回后K个数值的和。
注意处理时，由于需要处理后K个值，因此需要将给出的code拼接起来。
"""


class DefuseTheBomb(object):

    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = list()
        len_code = len(code)
        if k == 0:
            return [0] * len_code
        code += code
        if k > 0:
            for i in range(len_code):
                result.append(sum(code[i + 1: i + 1 + k]))
        else:
            for i in range(len_code, 2 * len_code):
                result.append(sum(code[i + k: i]))
        return result

