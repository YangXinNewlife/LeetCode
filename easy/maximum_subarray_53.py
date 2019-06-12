# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'


class MaximumSubarray(object):

    def run(self, nums):
        """
        Solution:
            Dynamic planning
        DP Function:
            dp[i] = max{num[i], dp[i - 1] + num[i]}
        :return:
        """
        dp = [-999] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        result = dp[0]
        for j in range(1, len(dp)):
            result = max(result, dp[j])
        return result


if __name__ == '__main__':
    maximum = MaximumSubarray()
    list_num = [-2, 1]
    print(maximum.run(list_num))

