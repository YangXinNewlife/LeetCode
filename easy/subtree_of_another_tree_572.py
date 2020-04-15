# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里我主要使用的是递归的思想，当然也可以使用先序遍历做标记的方式；
"""


class SubtreeOfAnotherTree(object):

    def check(self, s, t):
        if s is None or t is None:
            return s is None and t is None
        if s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Definition for a binary tree node.
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        :param s:
        :param t:
        :return:
        """
        if s is None or t is None:
            return s is None and t is None
        if self.check(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
