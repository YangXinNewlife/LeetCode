# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解析思路就是利用每个元素对10求余，然后判断是否为0（是否可以整除）；
"""


class SelfDividingNumbers(object):

    def selfDividingNumbers(self, left: int, right: int):
        result = []
        for i in range(left, right + 1):
            temp_val = i
            flag = 1
            while temp_val:
                temp_main = temp_val % 10
                if temp_main == 0 or i % temp_main != 0:
                    flag = 0
                    break
                temp_val //= 10
            if flag:
                result.append(i)
        return result



