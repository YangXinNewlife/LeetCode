# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
直接模拟计算操作即可
"""


class FinalValueOfVariableAfterPerformingOperations(object):

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for i in operations:
            if i == 'X++' or i == '++X':
                result += 1
            else:
                result -= 1
        return result


