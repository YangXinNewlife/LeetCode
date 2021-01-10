# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题的思路是可以使用中序遍历、先序遍历、后序遍历等方式遍历每一个节点，
并且判断是否叶子结点，如果是的话放到结果列表；
"""


class LeafSimilarTrees(object):

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves_1 = []
        leaves_2 = []
        self.mid_order(root1, leaves_1)
        self.mid_order(root2, leaves_2)
        return leaves_1 == leaves_2

    def mid_order(self, root, leaves):
        if not root:
            return
        self.mid_order(root.left, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)
        self.mid_order(root.right, leaves)

