# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里要求的返回数据是从二叉树的最后一层从左到右返回集合。
我们采用非递归的方式，可以维护数据结构中的栈stack,利用栈的特性，维护计数器去统计stack中有多少个元素，然后在此遍历每个元素孩子，
先进先出的远离去判断每一个栈中的左右孩子。

推演过程
stack[3] temp[] result[] count = 1
stack[] temp[3] result[] count = 0
stack[9] temp[3] result[] count = 0
stack[9, 20] temp[3] result[] count = 0
stack[9, 20] temp[] result[[3]] count = 2
"""


class BinaryTreeLevelOrderTraversal(object):

    def levelOrderBottom(self, root):
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
        if root is None:
            return []
        result = []
        temp = []
        stack = []
        count = 1
        stack.append(root)
        while stack:
            node = stack.pop(0)
            count -= 1
            temp += [node.val]
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            if count == 0:
                result.insert(0, temp)
                temp = []
                count = len(stack)
        return result
