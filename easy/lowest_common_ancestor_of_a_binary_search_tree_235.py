# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
首先理解题目，目的是找到二叉搜索树的指定两个节点的最小公共节点。
已知题目中数据结构是一个二叉搜索树，其特性就是 左孩子节点 < 根节点 < 右孩子节点
因此我们可以得出以下的结论：
1.当两个指定节点 p, q 都小于根节点，则说明两个孩子节点都在 root 左侧，那么可以利用递归。
2.当两个指定节点 p, q 都大于根节点，则说明两个孩子节点都在 root 右侧，那么可以利用递归。
3.当1、2中的递归时或者 p、q 出现左右孩子分别在root左右(p < root.val, q > root.val),
则root则为最小公共节点。
"""


class LowestCommonAncestOfABinarySearchTree(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

