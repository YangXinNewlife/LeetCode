# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是基于给定的数组，计算折扣后的价格，
是否打折需要满足给定的价格后面有比他小的即可。
否则就是原价。
"""


class FinalPricesWithASpecialDiscountInAShop(object):

    def finalPrices(self, prices: List[int]) -> List[int]:
        result = list()
        length = len(prices)
        for i in range(length):
            flag = 0
            for j in range(i + 1, length):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    flag += 1
                    break
            if flag == 0:
                result.append(prices[i])
        return result
