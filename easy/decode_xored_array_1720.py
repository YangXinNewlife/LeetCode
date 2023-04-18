# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目就是要还原异或XOR操作，
异或操作符号是^,
直接遍历数组，分别执行异或，结果返回即可
"""


class DecodeXORedArray(object):

    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = list()
        result.append(first)
        for i in encoded:
            result.append(i^result[-1])
        return result
