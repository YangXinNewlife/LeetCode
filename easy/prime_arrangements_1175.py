# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目本身不难，难的是理解题目在说什么。
首先我们要的给出 1 到 n的所有排列组合，
然后又给出条件，质数要在质数位上排序。其实就可以理解为，
质数一组排列组合，
非质数一组排列组合
那么我们可以将数据拆称为两部分
1.质数
2.非质数
然后最后将两组的排列组合乘到一起就是答案，最后因为数据可能比较大。
因此我们需要把结果对(10 ** 9 + 7)取模（求余数）。
那么我们先判断质数多少个，然后非质数多少个，然后分别计算阶乘。
然后最后乘法再取余数即可。
"""


class PrimeArrangements(object):

    def numPrimeArrangements(self, n: int) -> int:
        prime_cnt = 0
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_cnt += 1
        permutations = 1
        for i in range(prime_cnt, 0, -1):
            permutations *= i

        for j in range(n - prime_cnt, 0, -1):
            permutations *= j
        return permutations % (10 ** 9 + 7)
