# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
我们使用维护一个queue来处理遍历当前的层级。
然后循环遍历每个层级，并将当前节点的层级与当前节点的数据值均存储起来，
再根据节点层级做hash处理，用append追加保持队内有序。
"""


class NaryTreeLevelOrderTraversal(object):

    def levelOrder(self, root):
        """
        # Definition for a Node.
        class Node:
        def __init__(self, val, children):
            self.val = val
            self.children = children
        :param root:
        :return:
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        while queue:
            node, level = queue.pop(0)
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))
        return res



