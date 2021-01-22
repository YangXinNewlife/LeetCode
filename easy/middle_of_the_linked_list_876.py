# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目很好理解，就是给一个单链表。
需要找到中间节点，奇数的话直接返回，偶数的话，返回后一个即可，那么怎么扫描一遍返回中间节点呢？
我们可以用两个快慢指针。快指针每次走两个，慢指针每次走一个。
"""


class MiddleOfTheLinkedList(object):

    def middleNode(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        slow_p, fast_p = temp, temp
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        return slow_p.next if fast_p else slow_p





