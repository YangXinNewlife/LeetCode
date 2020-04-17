# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解决的思路就是先序遍历N叉树
"""


class NaryTreePreorderTraversal(object):

    def dfs(self, root):
        if not root:
            return
        self.result.append(root.val)
        for i in range(len(root.children)):
            self.dfs(root.children[i])

    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.dfs(root)
        return self.result




