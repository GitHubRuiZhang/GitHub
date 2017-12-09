# python3
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.


# My solution
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        coins.sort()
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] > i:
                    break
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[-1] < float('inf'):
            return dp[-1]
        return -1






