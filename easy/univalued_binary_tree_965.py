# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是找出二叉树是否是单值二叉树，单只二叉树的意思就是所有节点的值都是相同的。
正常来说我们遍历二叉树，然后判断数据是否相同就可以。
"""


class UnivaluedBinaryTree(object):

    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.pre_order(root, root.val)

    def pre_order(self, root, value):
        if root is None:
            return True
        if root.val != value:
            return False
        left_value = self.pre_order(root.left, root.val)
        right_value = self.pre_order(root.right, root.val)
        return left_value and right_value
