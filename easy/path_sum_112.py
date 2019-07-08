# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
这里的解题思路主要是为深度搜索以及遍历的的操作
1.root是否为None。
2.root非None,并且没有左右子树，则其root.val应该是sum。
3.root非None,并且存在左右子树，则利用递归，将左子树或者右子树作为根，
并且将sum - root.val 作为新的sum传递进函数，直到叶子节点（该节点不存在孩子）
"""


class PathSum(object):

    def hasPathSum(self, root, sum: int) -> bool:
        """
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
        :param root:
        :param sum:
        :return:
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)