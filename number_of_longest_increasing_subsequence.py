# python3
# Given an unsorted array of integers, find the number of longest increasing subsequence.

# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5  subsequences' length is 1,
# so output 5.

# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.


# My solution
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        elif len(nums) == 1:
            return 1
        dp = [[1, 1] for i in range(len(nums))]
        max_out = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
            max_out = max(max_out, dp[i][0])
        out = 0
        for it in dp:
            if it[0] == max_out:
                out += it[1]
        print(dp)
        return out


