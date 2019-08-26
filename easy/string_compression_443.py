# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里的思路使用两个指针：
i作用是记录更改后chars的长度，
j作用是记录当前chars的下标位置，
count 为需要重复的次数，
当字符串结束后通过移动指针i，将count写入chars，
最后返回i的位置，就是新的字符串的长度。
"""


class StringCompression(object):

    def compress(self, chars):
        n = len(chars)
        i, count = 0, 1
        for j in range(1, n + 1):
            # 当前后一个 j 与 j - 1 字符是相等的
            if j < n and chars[j] == chars[j - 1]:
                count += 1
            else:
                # 字符不同，这里更新移动的指针
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    # 根据遍历的长度增加i的大小
                    for k in str(count):
                        chars[i] = k
                        i += 1
                count = 1
        return i
