# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
斐波那契数列递归实现即可：
1 1 2 3 5 8
从第二个开始，后一个是前两个数据的和。
注意判别边界 0 
"""


class FibonacciNumbers(object):

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1 or N == 2:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)


