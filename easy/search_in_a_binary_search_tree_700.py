# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给一个BST（二叉搜索树），主要是排序的作用，每一个root的left节点小于root，每一个root的right大于root；
要求返回对应subTree，我们只需要返回从root开始，
分别递归root的left和right即可；
"""


class SearchInABinarySearchTree(object):

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        :param root:
        :param val:
        :return:
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)



