# -*- coidng:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给定一个数值n,
我们先把n转换为二进制，然后进行0和1的翻转，
0 -> 1
1 -> 0
这里我们可以使用异或操作，就是翻转操作。
在Python中可以使用bin进行十进制和二进制的转换，
其中前两位是0b，无用，需要从第三位开始，
因此这里是bin(n)[2:]
bin(2796202)
'0b1010101010101010101010'
"""


class ComplementOfBase10Integer(object):

    def bitwiseComplement(self, n: int) -> int:
        result = ""
        n_bin_str = bin(n)[2:]
        for i in n_bin_str:
            result += str(int(i) ^ 1)
        return int(result, 2)
