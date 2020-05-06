# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是计算每层二叉树的平均值，这里我们使用BFS，层级遍历，每次遍历后均可计算出均值
"""
import collections


class AverageOfLevelsInBinaryTree(object):

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = collections.deque()
        result = []
        queue.append(root)
        while queue:
            size = len(queue)
            row = []
            for i in range(size):
                node = queue.popleft()
                if not node:
                    continue
                row.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if row:
                result.append(sum(row) / float(len(row)))
        return result




