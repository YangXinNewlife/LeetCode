# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是teemo,提莫有一个放毒功能，给定数组[],每一个元素是放毒的时间。在给定每个堵的生效时间。例如:duration = 2,
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
由于可以在已经攻击的情况下再次攻击，就是可以重置中毒时间，那么我们就可以考虑中毒的生效时间和多次放毒的周期哪个短？
短的就是生效时间，我们累加，最后再加上最后一次的生效时间即可。
"""


class TeemoAttacking(object):

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        result = 0
        for i in range(len(timeSeries) - 1):
            result += min(duration, timeSeries[i + 1] - timeSeries[i])
        result += duration
        return result


