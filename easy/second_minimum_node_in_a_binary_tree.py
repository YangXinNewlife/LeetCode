# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
此题的解题思路就是使用两个临时变量，
存储遍历时候的两个临时最小和第二小的两个数据；
遍历的时候去更新即可；
"""


class SecondMinimumNodeInABinaryTree(object):

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min_1 = float('inf')
        self.min_2 = float('inf')
        def dfs(root):
            if root.val < self.min_1:
                self.min_2 = self.min_1
                self.min_1 = root.val
            elif root.val < self.min_2 and root.val != self.min_1:
                self.min_2 = root.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        if root:
            dfs(root)
        return self.min_2 if self.min_2 != float('inf') else -1

