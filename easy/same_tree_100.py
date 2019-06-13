# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


class SameTree(object):

    def run(self, p, q):
        """
        Solution:
        1.Definition for a binary tree node.
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        2.利用递归的方式传递左右两边的节点，依次判断
        :param p:
        :param q:
        :return:
        """
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.run(p.left, q.left) and self.run(p.right, q.right)
        return False
