# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions：
这里的解题思路是首先理解题意，
这里的题目意思是去寻找二叉树中的最长直径（直径的定义为任意两个节点的距离）。
这里我们只需要考虑每两个节点的左孩子与右孩子的长度求和最长的即可。
"""


class DiameterOfBinaryTree(object):

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_sum = 0
        if root:
            self.tree_depth(root)
        return self.max_sum

    def tree_depth(self, root):
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = self.tree_depth(root.left)
        if root.right:
            right_depth = self.tree_depth(root.right)
        self.max_sum = max(self.max_sum, left_depth + right_depth)
        return max(left_depth, right_depth) + 1



