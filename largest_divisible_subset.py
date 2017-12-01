# python3
# Given a set of distinct positive integers,
# find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# nums: [1,2,3]

# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# nums: [1,2,4,8]

# Result: [1,2,4,8]


# My solution
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = [[] for _ in range(len(nums))]
        out = []
        for i in range(len(nums)):
            for j in reversed(range(i + 1)):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(out):
                out = dp[i]
        return out


