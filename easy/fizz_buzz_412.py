# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题思路为循环遍历，并且根据题目的判断条件依次写出即可。
"""


class FizzBuzz(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
        return result


