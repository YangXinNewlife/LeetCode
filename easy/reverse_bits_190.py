# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
1.题意为给定无符号32位整数，求该整数翻转(对应的二进制数的翻转)后所得的整数值。
2.我们可以利用位运算的方式来操作，由于限制位数为32位，我们只需要遍历32次，做32次左移后面加上对应的判断位数（1/0），并将每一位变成当前位（低位）方便操作。
3.每当低位 &1 的结果为 1，说明低位为1，此时将待输出的目标整数左移动一位并加上1；
4。每当低位 &1 的结果为0，说明低位为0，此时将待输出的目标整数左移一位即可；
5。循环直到移动完32次，所得目标整数即为所求。
"""


class ReverseBits(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            if 1 == n & 1:
                ans = (ans << 1) + 1
                n >>= 1
            else:
                ans = ans << 1
                n >>= 1
        return ans


