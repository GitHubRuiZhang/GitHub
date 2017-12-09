# python3
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


# My solution
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_positive = [0 for i in range(len(nums))]
        dp_negative = [0 for i in range(len(nums))]
        dp_positive[0] = nums[0]
        dp_negative[0] = nums[0]
        out = nums[0]
        for i in range(1, len(nums)):
            dp_positive[i] = max(nums[i], max(dp_positive[i - 1] * nums[i], dp_negative[i - 1] * nums[i]))
            dp_negative[i] = min(nums[i], min(dp_positive[i - 1] * nums[i], dp_negative[i - 1] * nums[i]))
            out = max(dp_positive[i], dp_negative[i], out)
        return out

        # This is not dynamic programming
        dp = [[1 for i in range(len(nums))] for j in range(len(nums))]
        out = -float('inf')
        for i in range(len(nums))[::-1]:
            dp[i][i] = nums[i]
            out = max(out, dp[i][i])
            for j in range(i + 1, len(nums)):
                dp[i][j] = dp[i][j - 1] * nums[j]
                out = max(out, dp[i][j])
        return out







