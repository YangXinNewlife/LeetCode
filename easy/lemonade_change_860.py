# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
提议是你是一家柠檬水店家，每一杯$5, 顾客会用$5, $10, $20购买，我们需要给顾客找钱，看看我们是否可以将零钱找给顾客，可以将零钱正确的给顾客则返回True；
例如 顾客付$10, 我们给顾客$5, 
    顾客付$20, 我们给顾客$10, $5;
我们这里使用字典结构来统计10，5的个数，通过判断即可知道返回True， False；
"""


class LemonadeChange(object):

    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                changes[5] += 1
            elif i == 10:
                if changes[5] == 10:
                    return False
                else:
                    changes[10] += 1
                    changes[5] -= 1
            elif i == 20:
                if changes[10] != 0:
                    if changes[5] == 0:
                        return False
                    else:
                        changes[5] -= 1
                        changes[10] -= 1
                else:
                    if changes[5] < 3:
                        return False
                    else:
                        changes[5] -= 3
        return True
