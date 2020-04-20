# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions
题目的后序遍历，这里可以理解为将输入的数据已经放在了栈stack中，然后按批次的出栈，即可；
举个例子，输入的数据是[1,null,3,2,4,null,5,6]
第一批的出栈是[5,6]
第二批的出栈是[3,2,4]
第三批的出栈是[1]
那么刚好是[5,6,3,2,4,1]
"""


class NaryTreePostorderTraversal(object):

    def postorder(self, root: 'Node') -> List[int]:
        """
        # Definition for a Node.
        class Node:
            def __init__(self, val=None, children=None):
                self.val = val
                self.children = children
        """
        result = []
        if not root:
            return result
        for i in root.children:
            result.extend(self.postorder(i))
        result.append(root.val)
        return result

