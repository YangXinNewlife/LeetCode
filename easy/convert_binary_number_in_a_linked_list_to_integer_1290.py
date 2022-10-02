# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目就是计算下给出的二进制数组的十进制数值
直接遍历链表并进行计算即可。
"""


class ConvertBinaryNumberInALinkedListToInteger(object):

    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            result = result * 2 + head.next.val
            head = head.next
        return result

