# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
题目的含义是这样的：
首先我们对于当前的32为整数，找到一个所有元素都是当前元素的，并且稍微大于当前元素的整数。没有的话返回-1。
例如：
123 -> 213;
321 -> -1;
解题的思路如下：
从右到左找到第一个降序的数字，index极为 i - 1，然后从右到左找到第一个比这个数字大的数字，index记为j，交换两个数字的值，
然后将i - 1之后的序列倒序排序即可，当降序的数字不存在时，i == 0，返回 -1；
当得到的结果超过32-bit时，也返回-1；
"""


class NextGreaterElementIII(object):

    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        i = len(s) - 1
        while i - 1 >= 0 and s[i-1] >= s[i]:
            i -= 1

        if i == 0:
            return -1
        j = len(s) - 1
        while s[j] <= s[i - 1]:
            j -= 1
        s[i - 1], s[j] = s[j], s[i - 1]
        s[i:] = s[i:][::-1]
        result = int(''.join(s))
        if result <= 2**31-1:
            return result
        return -1




