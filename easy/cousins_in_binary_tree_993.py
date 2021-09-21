# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections


class CousinsInBinaryTree(object):

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.tree = collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        px, dx = self.tree[x]
        py, dy = self.tree[y]
        return dx == dy and px != py

    def dfs(self, root, parent, depth):
        if not root:
            return
        self.tree[root.val] = (parent, depth)
        self.dfs(root.left, root, depth + 1)
        self.dfs(root.right, root, depth + 1)
