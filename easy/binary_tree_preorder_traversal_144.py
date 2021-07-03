# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Solutions:
解题思路先序遍历二叉树，递归即可
"""


class BinaryTreePreorderTraversal(object):

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = list()
        self.pre(root, result)
        return result

    def pre(self, root, tenp_result):
        if root is None:
            return None
        tenp_result.append(root.val)
        self.pre(root.left, tenp_result)
        self.pre(root.right, tenp_result)

