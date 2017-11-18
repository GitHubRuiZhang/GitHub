# python3
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share
# of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:

# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]


# My solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        # profit
        s0 = [-prices[0]]  # If you buy
        s1 = [0]  # If you dont buy and dont sell
        s2 = [0]  # If you sell
        for i in range(1, len(prices)):
            s0.append(max(s0[i - 1], s1[i - 1] - prices[i]))
            s1.append(max(s0[i - 1], s1[i - 1], s2[i - 1]))
            s2.append(s0[i - 1] + prices[i])
        print(s0, s1, s2)
        return max(s2[-1], s1[-1])
