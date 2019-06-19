# -*- coding:utf-8 -*-
__author__='yangxin_ryan'
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Solution:
判断二叉树的层级，首先当root为None的时候，层级为0
当二叉树的root为非None的时候，再去用递归的方式首先获取层级。
状态方程：
func = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
"""


class MaximumDepthOfBinaryTree(object):
    def maxDepth(self, root: TreeNode) -> int:
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
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))