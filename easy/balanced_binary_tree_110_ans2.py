# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
对于方法一的方法这里节省了每一个节点都去计算深度的过程，
如果已经判断出子树不平衡，则不去计算具体的深度，而是直接返回-1。
并且对于每一个节点，我们通过check_depth方法递归获得左右子树的深度，
如果子树是平衡的我们就返回真实的深度，若不平衡，则直接返回-1。
时间复杂度：O(n)
空间复杂度：O(h)
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
        if -1 == self.check_depth(root):
            return False
        else:
            return True

    def check_depth(self, root):
        if root is None:
            return 0
        left = self.check_depth(root.left)
        if -1 == left:
            return -1
        right = self.check_depth(root.right)
        if -1 == right:
            return -1
        diff = abs(left - right)
        if diff > 1:
            return -1
        else:
            return 1 + max(left, right)
