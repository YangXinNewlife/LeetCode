# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Solutions:
题目的含义是找出来二叉树的兄弟节点。
兄弟节点定义：
高度相同，父节点不同。
我们使用深度遍历，并记录下高度和父节点，最后比较即可。
由于每个节点不同我们可以使用set来记录。
"""


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
