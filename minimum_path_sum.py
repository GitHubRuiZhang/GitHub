# python3
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


# My solution
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        cur = 0
        for i in range(len(grid[0])):
            cur += grid[0][i]
            dp[0][i] = cur
        cur = 0
        for j in range(len(grid)):
            cur += grid[j][0]
            dp[j][0] = cur
        for j in range(1, len(grid)):
            for i in range(1, len(grid[0])):
                dp[j][i] = min(dp[j - 1][i], dp[j][i - 1]) + grid[j][i]

        return dp[-1][-1]
