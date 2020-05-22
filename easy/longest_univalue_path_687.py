# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是我们找出来路径中每个节点具有相同val值的最长路径（这里指的是'边'的长度）；
可以不经过根，因此要遍历所节点，然后返回记录的最大值；
这里使用DFS递归的操作；
"""


class LongestUnivaluePath(object):

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0

        def dfs_tree_depth(root):
            left_depth = 0
            right_depth = 0
            if root.left:
                left_depth = dfs_tree_depth(root.left)
                if root.left.val != root.val:
                    left_depth = 0
            if root.right:
                right_depth = dfs_tree_depth(root.right)
                if root.right.val != root.val:
                    right_depth = 0
            self.result = max(self.result, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        if root:
            dfs_tree_depth(root)
        return self.result




