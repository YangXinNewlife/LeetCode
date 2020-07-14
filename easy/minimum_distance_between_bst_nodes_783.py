# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目很简单就是在BST树中找到相邻的节点之间的元素差值最小的值
直接中序遍历记录每个元素，并且找到相邻的值最小的就是答案了
"""


class MinimumDistanceBetweenBSTNodes(object):

    def minDiffInBST(self, root: TreeNode) -> int:
        self.tree_node_list = []
        self.mid_order(root)
        return min(self.tree_node_list[i + 1] - self.tree_node_list[i] for i in range(len(self.tree_node_list) - 1))

    def mid_order(self, root):
        if root is None:
            return
        self.mid_order(root.left)
        self.tree_node_list.append(root.val)
        self.mid_order(root.right)
