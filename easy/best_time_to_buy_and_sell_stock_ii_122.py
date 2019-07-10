# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
解题思路可以理解为支持多次交易，但是不支持重叠式交易
比如可以：
        买、卖、买、卖
        但是不能：
        卖、卖 或者 买、买
因此我们只需要考虑后一天大雨前一天，就可以进行交易。
否则不进行交易，最后返回利益和即可。
"""


class BestTimeToBuyAndSellStockII(object):

    def maxProfit(self, prices):
        """
        可以进行不止一次交易，但每次交易不能重叠
        比如可以：
        买、卖、买、卖
        但是不能：
        卖、卖 或者 买、买
        :param prices:
        :return:
        """
        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit
