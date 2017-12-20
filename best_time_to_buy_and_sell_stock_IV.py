# python3
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# My solution
class Solution(object):
    def maxProfit(self, K, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # O(kn)
        if len(prices) < 2:
            return 0

        if K >= len(prices) // 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)

        dp = [0 for i in range(len(prices))]
        k = 1
        while k < K + 1:
            res = 0
            cur = prices[0] - dp[0]
            for i in range(1, len(prices)):
                res = max(res, prices[i] - cur)
                cur = min(cur, prices[i] - dp[i])
                dp[i] = res
            k += 1
        return dp[-1]

        # O(kn)
        if len(prices) < 2:
            return 0
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
        dp = [[0 for i in range(len(prices))] for j in range(K + 1)]
        for k in range(1, K + 1):
            for i in range(1, len(prices)):
                for j in range(i):
                    dp[k][i] = max(dp[k][i], dp[k][i - 1], dp[k - 1][j] + prices[i] - prices[j])
        return dp[-1][-1]

