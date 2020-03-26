# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义：
树节点的倾斜度定义为所有左子树节点值的总和与所有右子树节点值的总和之间的绝对差。 空节点的倾斜度为0。
整个树的倾斜度定义为所有节点的倾斜度之和。
计算完还要加上根节点的值
"""


class BinaryTreeTilt(object):

    result = 0

    def findTilt(self, root: TreeNode) -> int:
        """
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.left = None
        #         self.right = None
        :param root:
        :return:
        """
        self.post_order(root)
        return self.result

    def post_order(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.post_order(root.left)
        right = self.post_order(root.right)
        self.result += abs(left - right)
        return left + right + root.val

