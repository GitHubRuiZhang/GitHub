# python3
# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids.
# How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.


# My solution
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == [[]]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for j in range(n)] for i in range(m)]
        block = False
        for i in range(m):
            if block is True:
                dp[i][0] = 0
            elif obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                block = True
        block = False
        for i in range(n):
            if block is True:
                dp[0][i] = 0
            elif obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                block = True

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]