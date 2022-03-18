# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
根据题意说明替换字符串中的 . 为 [.] 即可。
"""


class DefangingAnIPAddress(object):

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
