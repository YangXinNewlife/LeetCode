# -*- coding:utf-8 -*-
__author__ = 'jiuzhang'
class Solution(object):
    def countAndSay(self, n):
        seq = ['1']
        top = 1
        while n - 1 > 0:
            n -= 1
            bak = []
            i = 0
            while i < top:
                num = 1
                while i + 1 < top and seq[i+1] == seq[i]:
                    i += 1
                    num += 1
                bak.append(chr(num + ord('0')))
                bak.append(seq[i])
                i += 1
            seq = bak
            top = len(bak)
        return ''.join(seq)

