# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个用二维数组表示的图片，其中每个像素（点）就是数字组成的；
例如给定的例子：
[[1,1,1],[1,1,0],[1,0,1]]
-> 图片如下（数字为相同的 1 或者 0 或者为其他数字的点是同一种颜色）：
1 1 1
1 1 0
1 0 1

然后要求输入一个像素的起始点，在给定一个新的颜色（就是数字），
1.然后我们要去判断起始点的上下左右四个方向，只要是与之相连，并且颜色一致的点，均要修改颜色，
2.然后与之相邻的上下左右被修改了颜色的点，的上下左右如果有与之相连并且颜色与之前保持一致的，也要修改；
说到这里肯定是想到了递归的方式，我们就可以利用深度搜索来实现！
"""


class FloodFill(object):

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        length, weight = len(image), len(image[0])
        temp_color = image[sr][sc]
        if temp_color == newColor:
            return image

        def dfs(temp_sr, temp_sc):
            if image[temp_sr][temp_sc] == temp_color:
                image[temp_sr][temp_sc] = newColor
                if temp_sr >= 1:
                    dfs(temp_sr - 1, temp_sc)
                if temp_sr < length - 1:
                    dfs(temp_sr + 1, temp_sc)
                if temp_sc >= 1:
                    dfs(temp_sr, temp_sc - 1)
                if temp_sc < weight - 1:
                    dfs(temp_sr, temp_sc + 1)
        dfs(sr, sc)
        return image



