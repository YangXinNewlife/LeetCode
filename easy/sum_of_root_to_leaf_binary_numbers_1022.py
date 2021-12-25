# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题思路是我们利用深度遍历规则，其中避免累加的节点多，
因此需要加上
10^9+7 取模,来避免整数溢出的问题。其中10^9+7
"""


class SumOfRootToLeafBinaryNumbers(object):
    """
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    """
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        self.dfs(root, root.val)
        return self.result

    def dfs(self, root, pre):
        if not root.left and not root.right:
            self.result = (self.result + pre) % (10 ** 9 + 7)
            return
        if root.left:
            self.dfs(root.left, pre * 2 + root.left.val)
        if root.right:
            self.dfs(root.right, pre * 2 + root.right.val)














