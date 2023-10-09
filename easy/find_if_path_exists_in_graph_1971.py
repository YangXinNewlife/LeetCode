# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意是给定一组无向图中的每个节点（x,y）。
再给定图的两个下标，判断下给出的两个节点是否相连接
题目看似是图论的问题，其实可以用并查集来解决，这里用队列模拟并查集的合并和查找逻辑。
"""
import collections


class FindIfPathExistsInGraph(object):

    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        # def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        collect_dict = collections.defaultdict(set)
        for i, j in edges:
            collect_dict[i].add(j)
            collect_dict[j].add(i)
        dequeue = collections.deque()
        dequeue.append(source)
        result = set()
        while dequeue:
            dequeue_size = len(dequeue)
            for k in range(dequeue_size):
                cur_node = dequeue.popleft()
                for next_node in collect_dict[cur_node]:
                    if next_node == destination:
                        return True
                    else:
                        if next_node not in result:
                            result.add(next_node)
                            dequeue.append(next_node)
        return False
