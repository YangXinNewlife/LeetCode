# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
由于题目要求是判断是否是高度平衡的二叉树，那么两个子树之间的深度差不能超过1，
这里的方法是计算各孩子的深度，并且对比即可。
时间复杂度是：O(NlogN)
"""


class BalancedBinaryTree(object):

    def isBalanced(self, root) -> bool:
        """
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None
        :param root:
        :return:
        """
        if root is None:
            return True
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))

