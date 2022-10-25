# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
题目的意思就是给两个树，cloned是由original复制来的，
再给一个目标节点包含一个val值
需要中序遍历两个数，看下哪一个节点和给定的目标值target.val一致
则返回这个值即可。
"""


class FindACorrespondingNodeOfABinaryTreeAnACloneOfThatTree(object):

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.result = 0
        self.target = target
        self.inorder(original, cloned)
        return self.result

    def inorder(self, ori_node, clone_node):
        if ori_node:
            if ori_node.val == self.target.val:
                self.result = clone_node
                return
            if ori_node.left and not self.result:
                self.inorder(ori_node.left, clone_node.left)
            if ori_node.right and not self.result:
                self.inorder(ori_node.right, clone_node.right)






