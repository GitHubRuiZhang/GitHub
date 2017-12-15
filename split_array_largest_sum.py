# python
# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

# Note:
# If n is the length of array, assume the following constraints are satisfied:

# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# Examples:

# Input:
# nums = [7,2,5,10,8]
# m = 2

# Output:
# 18

# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.


# My solution
class Solution(object):
    def search(self, nums, index, m, res):
        cur = nums[index:]
        if m > len(cur):
            return float('inf'), res
        if m == len(cur):
            return max(cur), res
        if m == 1:
            return sum(cur), res
        out = float('inf')
        pre = 0
        for i in range(index + 1, len(nums)):
            pre += nums[i - 1]
            if (i, m - 1) in res:
                out = min(out, max(pre, res[(i, m - 1)]))
            else:
                it, res = self.search(nums, i, m - 1, res)
                out = min(out, max(pre, it))

        if (index, m) in res:
            res[(index, m)] = min(res[(index, m)], out)
        else:
            res[(index, m)] = out

        return out, res

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # dp
        dp = [[float('inf') for j in range(m)] for i in range(len(nums) + 1)]
        pre = 0
        dp[0][0] = 0
        for i in range(1, len(nums) + 1):
            pre += nums[i - 1]
            dp[i][0] = pre

        for j in range(m):
            dp[0][j] = 0

        for i in range(1, len(nums) + 1):
            for it in range(i):
                for j in range(1, m):
                    dp[i][j] = min(dp[i][j], max(dp[it][j - 1], dp[i][0] - dp[it][0]))

        return dp[len(nums)][m - 1]

        # naive
        out, res = self.search(nums, 0, m, {})
        return out


