# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
from collections import defaultdict
"""
Solutions:
利用深度优先搜索，并且使用cur_sum[i]存储每个路径的值，
判断是否与sum,也就是目标值target是否相同；
"""


class PathSumIII(object):

    result = 0

    def dfs(self, cur_sum, root, cur_val, target):
        """
        深度优先搜索
        这里使用了记忆化cur_sum以及cur_val
        :param cur_sum:
        :param root:
        :param cur_val:
        :param target:
        :return:
        """
        if not root:
            return
        # cur_val表示从root到当前结点的路径的和
        cur_val += root.val
        self.result += cur_sum[cur_val - target]
        cur_sum[cur_val] += 1
        if root.left:
            self.dfs(cur_sum, root.left, cur_val, target)
        if root.right:
            self.dfs(cur_sum, root.right, cur_val, target)
        cur_sum[cur_val] -= 1

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        cur_sum = defaultdict(int)
        cur_sum[0] = 1
        if root:
            self.dfs(cur_sum, root, 0, sum)
        return self.result
