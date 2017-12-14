# python3
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons.
# If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
#  Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:
# (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

# Example:

# Given [3, 1, 5, 8]

# Return 167

#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


# My solution
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [it for it in nums if it != 0] + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for it in range(1, len(nums) - 1):
            for l in range(len(nums) - it - 1):
                r = l + it + 1
                for i in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r])

        return dp[0][len(nums) - 1]


