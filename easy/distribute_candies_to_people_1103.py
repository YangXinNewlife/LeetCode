# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意给第一个人一个糖果，给第二个人两个糖果，依此类推，直到我们给最后一个人n个糖果。
我们回到这一行的开头，给第一个人n+1个糖果，给第二个人n+2个糖果，依此类推，直到我们给最后一个人2*n个糖果。
这个过程会重复（每次我们多给一块糖果，到达最后一排后移到第一排），直到糖果用完。
最后一个人将收到我们剩下的所有糖果（不一定比之前的礼物多一个）。
返回一个数组（长度num_people和sum candies），该数组表示糖果的最终分发。
我们直接模拟操作即可。
"""


class DistributeCandiesToPeople(object):

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * (num_people + 1)
        i, j = 0, 0
        while candies > 0:
            k = i % num_people + 1
            nums_temp = i + 1
            result[k] = result[k] + nums_temp if candies >= nums_temp else result[k] + candies
            candies -= nums_temp
            i += 1
        return result[1:num_people + 1]

