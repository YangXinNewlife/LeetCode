# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是判断字符串是否是Palindrome回文字符串（最多删除一个字符构成也可以）；
这里我解题的思路就是二分的方式，首先我们用两个指针
left_index 和 right_index 来处理判断元素是否相等，
然后构造lambda函数is_palindrome利用类似递归的方式使用
首先回文字符串是对称的，说明反转后肯定相同；
is_palindrome(s[left_index + 1: right_index + 1]) -> 这里应该是s[left_index: right_index + 1]，
而使用s[left_index: right_index + 1]的原因就是因为删除了left_index这个索引的元素；
is_palindrome(s[left_index: right_index])来判断字符串反转后是否相同
"""


class ValidPalindromeII(object):

    def validPalindrome(self, s: str) -> bool:
        is_palindrome = lambda s: s == s[::-1]
        left_index = 0
        right_index = len(s) - 1
        while left_index <= right_index:
            if s[left_index] == s[right_index]:
                left_index += 1
                right_index -= 1
            else:
                return is_palindrome(s[left_index + 1: right_index + 1]) or is_palindrome(s[left_index: right_index])
        return True


