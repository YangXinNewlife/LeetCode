# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

题意就是数据反向存储的，需要按位进行求和计算
然后最后再反向存储进去即可，使用一个临时的链表做缓存即可。
"""


class AddTwoNumbers(object):

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode(0)
        temp_val = 0
        while l1 or l2 or temp_val:
            if l1:
                temp_val += l1.val
                l1 = l1.next
            if l2:
                temp_val += l2.val
                l2 = l2.next
            node.next = node = ListNode(temp_val%10)
            temp_val //= 10
        return head.next






