# -*- coding:utf-8 -*-
__author__ = 'yangxin'
import collections
"""
Solutions:
题目的意思是：
给定具有重复项的二叉搜索树（BST），找到给定BST中的所有模式（最常出现的元素）。
结局办法：
返回BST中出现次数最多的数，对BST中序遍历即可，不需要中序遍历完成后再求众数，直接在遍历的过程中更新结果。
这里采用二叉树的中序遍历。
"""


class FindModeinBinarySearchTree(object):

    def findMode(self, root):
        """
        Definition for a binary tree node.
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        :param root:
        :return:
        """
        if not root:
            return []
        count = collections.defaultdict(int)

        def traverse(node_root):
            if node_root:
                traverse(node_root.left)
                count[node_root.val] += 1
                traverse(node_root.right)
        traverse(root)
        max_ele = max(count.values())
        return [i for i in count if count[i] == max_ele]


