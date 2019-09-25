# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
由于这里是做对比二进制位不相同的数量，
我们可以使用按位异或操作，
最后统计出有多少个1就可以了，异或操作，不同的是1，相同的是0。
"""


class HammingDistance(object):

    def hammingDistance(self, x: int, y: int):
        return bin(x ^ y).count('1')
