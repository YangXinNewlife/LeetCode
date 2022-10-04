# -*- coding:utf-8 -*-
__author__ = 'yangxin'
"""
Solutions:
题目的意思就是给定一个数字n,返回n个数字求和等于0的数组。
我们可以把逻辑拆分奇数和偶数考虑
奇数可以
[...,-i,0,i...]
偶数可以
[...,-i,i...]
奇数比偶数就多个0。
因此上述逻辑的代码实现如下
"""


class FindNUniqueIntegersSumUpToZero(object):

    def sumZero(self, n: int) -> List[int]:
        result = list()
        if n % 2 == 1:
            result.append(0)
            n -= 1
        i = 1
        while n > 0:
            result = [-i] + result
            result.append(i)
            n -= 2
            i += 1
        return result










