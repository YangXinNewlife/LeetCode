# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions;
题意是写一个遍历完全树的方法complete是每一个非叶子节点都挂两个。
"""
import collections


class CountCompleteTreeNodes(object):
    """
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    """
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        result = 0
        while queue:
            for i in range(len(queue)):
                result += 1
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

