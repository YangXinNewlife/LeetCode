# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题分析可以理解为我们要处理输入的一堆邮件数据，我们按照要求进行处理，
其中name中如果包含有'.'，那么把这个'.'给去掉；
如果name中有'+'，那么从+到后面的name部分全部去掉，最后返回不同的个数（去重，可以使用Set集合）
"""


class UniqueEmailAddresses(object):

    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for i in emails:
            name, domain = i.split("@")
            name = name.split("+")[0].replace(".", "")
            result.add(name + "@" + domain)
        return len(result)

