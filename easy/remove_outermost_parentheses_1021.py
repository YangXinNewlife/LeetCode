# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是给出一个全是括号的字符串，我们需要把外层的去掉。
解题思路是找到对称的点，我们用一个计数器，当"（"和"）"的数量刚好一致时，
说明括号对称，因此获取中间的位置即可。
"""


class RemoveOutermostParentheses(object):

    def removeOuterParentheses(self, s: str) -> str:
        pre = 0
        result = ""
        count = 0
        for i, j in enumerate(s):
            if j == '(':
                count += 1
            else:
                count -= 1
            print(count)
            if count == 0:
                result += s[pre + 1: i - 1]
                pre = i + 1
        return result


