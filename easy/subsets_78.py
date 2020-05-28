# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
此题目要打印所有元素，例如[1, 2, 3]的所有排列组合，那么可能有如下：
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]共八种；
因此我们可以将这种拆分成为
[[], 
[1], [1, 2], [1, 2, 3], 
[1, 3], 
[2], [2, 3], 
[3]]
如上面的的组和更像是一种递归，只要我们在代码中放入一个临时的数组temp, 然后维护temp即可；
模拟过程如下：
result = []
temp = [] append -> result = [[]]
然后进入for循环，i = 0, 元素为 1, 加入temp则为temp = [1]
--
result = [[]]
temp = [1] append -> result = [[], [1]]
然后进入for循环，i = 1, 元素为 2, 加入temp则为temp = [1, 2]
--
result = [[], [1]]
temp = [2] append -> result = [[], [1], [1, 2]]
然后进入for循环，i = 2, 元素为 3, 加入temp则为temp = [1, 2, 3]

-- 到此处递归完成，我们开始退回上一个 i = 1时，然后temp.pop()，元素2出栈，
result = [[], [1]，[1, 2], [1, 2, 3]]
temp = [1, 3]
-- 
result = [[], [1]，[1, 2], [1, 2, 3], [1, 3]]
temp = [1, 3] 然后返回递归到最外层temp.pop,元素1出栈，temp = []
for i 自动变到 1，元素为2，因此，temp = [2],
--
result = [[], [1]，[1, 2], [1, 2, 3], [1, 3], [2]]
temp = [2, 3]
--
result = [[], [1]，[1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
然后到底出栈
i = 2，元素为3
temp = [3]
--
result = [[], [1]，[1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
退出循环，返回结果如下
result = [[], [1]，[1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
"""


class Subsetsx(object):

    def subsets(self, nums):
        self.result = []
        def dfs(nums, temp, i):
            self.result.append(temp[:])
            for i in range(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()
        dfs(nums, [], 0)
        return self.result
