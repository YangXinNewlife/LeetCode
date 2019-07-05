# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
求二叉树的最小深度
我们可以先列举所有情况：
1.当节点为叶子结点，深度为1
2.当根节点为None,深度为0
3.当节点只有左孩子（或右孩子）时，深度为左孩子（右孩子）+ 1
4.当节点既有左孩子又有右孩子时，深度为min(左孩子，右孩子) + 1
5.递归上面的情况
"""


class MinimumDepthOfBinaryTree(object):

    def minDepth(self, root):
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
        if root.left is None and root.right is None:
            return 1
        if root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        if root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
