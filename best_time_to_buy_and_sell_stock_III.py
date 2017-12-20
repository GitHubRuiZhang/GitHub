# python3
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# My solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(kn)
        if len(prices) < 2:
            return 0
        K = 2
        dp = [[0 for i in range(len(prices))] for j in range(K + 1)]
        for k in range(1, K + 1):
            cur = prices[0] - dp[k - 1][0]
            for i in range(1, len(prices)):
                dp[k][i] = max(dp[k][i], dp[k][i - 1], prices[i] - cur)
                cur = min(cur, prices[i] - dp[k - 1][i])
        return dp[-1][-1]

        # O(kn^2)
        if len(prices) < 2:
            return 0
        K = 2
        dp = [[0 for i in range(len(prices))] for j in range(K + 1)]
        for k in range(1, K + 1):
            for i in range(1, len(prices)):
                for j in range(i):
                    dp[k][i] = max(dp[k][i], dp[k][i - 1], dp[k - 1][j] + prices[i] - prices[j])
        return dp[-1][-1]
