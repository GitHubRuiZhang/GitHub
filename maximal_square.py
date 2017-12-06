# python3
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.


# My solution
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        # [left, up,square_length]
        dp = [[[0, 0, 0] for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        out = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1][1] = dp[i][j + 1][1] + 1
                    dp[i + 1][j + 1][0] = dp[i + 1][j][0] + 1
                    if min(dp[i + 1][j + 1][1], dp[i + 1][j + 1][0]) >= dp[i][j][2] + 1:
                        dp[i + 1][j + 1][2] = dp[i][j][2] + 1
                        out = max(out, dp[i + 1][j + 1][2] ** 2)
                    else:
                        dp[i + 1][j + 1][2] = min(dp[i + 1][j + 1][1], dp[i + 1][j + 1][0])
        return out

