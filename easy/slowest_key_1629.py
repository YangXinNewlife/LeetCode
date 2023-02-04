# -*- coding:utf-8 -*-
___author__ = 'yangxin_ryan'
"""
Solutions:
题意就是判断下每次按下键盘的每个字母停留的最长时间，
因此我们判断下每个字断的耗时即可，
如果耗时相同，则返回字符大的那个，这个需要单独处理下。
"""


class SlowestKey(object):
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result = keysPressed[0]
        used_time = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            if releaseTimes[i] - releaseTimes[i - 1] > used_time or (releaseTimes[i] - releaseTimes[i - 1] == used_time and result < keysPressed[i]):
                result = keysPressed[i]
                used_time = releaseTimes[i] - releaseTimes[i - 1]
        return result



