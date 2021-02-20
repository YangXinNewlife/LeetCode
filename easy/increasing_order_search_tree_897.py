# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是中序遍历给出的二叉树，然后再根据要求用建立一个只有右孩子的二叉树。
思路就是先中序遍历，保留结果，然后再建立一个二叉树即可（只有右孩子）
"""


class IncreasingOrderSearchTree(object):

    def increasingBST(self, root: TreeNode) -> TreeNode:
        tree = self.mid_order(root)
        if not tree:
            return None
        result_root = TreeNode(tree[0])
        cur_node = result_root
        for i in range(1, len(tree)):
            cur_node.right = TreeNode(tree[i])
            cur_node = cur_node.right
        return result_root

    def mid_order(self, root):
        if not root:
            return []
        tree = []
        tree.extend(self.mid_order(root.left))
        tree.append(root.val)
        tree.extend(self.mid_order(root.right))
        return tree


