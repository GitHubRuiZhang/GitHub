# python3
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball,
# you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right).
# However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 109 + 7.

# Example 1:
# Input:m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:

# Example 2:
# Input:m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:

# Note:
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].


# My solution
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        # Improve
        dp = [[0 for jj in range(n)] for ii in range(m)]
        dp[i][j] = 1
        step = 0
        count = 0
        res = 10 ** 9 + 7
        while step < N:
            new = [[0 for jj in range(n)] for ii in range(m)]
            for it in range(m):
                for jt in range(n):
                    if it == m - 1:
                        count += dp[it][jt]
                    if it == 0:
                        count += dp[it][jt]
                    if jt == n - 1:
                        count += dp[it][jt]
                    if jt == 0:
                        count += dp[it][jt]
                    count %= res
                    if it > 0:
                        new[it][jt] += dp[it - 1][jt]
                    if it < m - 1:
                        new[it][jt] += dp[it + 1][jt]
                    if jt > 0:
                        new[it][jt] += dp[it][jt - 1]
                    if jt < n - 1:
                        new[it][jt] += dp[it][jt + 1]
                    new[it][jt] %= res
            dp = new
            step += 1
        return count

        # Naive
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        res = [(i, j)]
        step = 0
        count = 0
        while step < N:
            new = []
            while res:
                cur = res.pop()
                for it in directions:
                    x = cur[0] + it[0]
                    y = cur[1] + it[1]
                    if x < 0 or x >= m or y < 0 or y >= n:
                        count += 1
                    else:
                        new.append((x, y))
            res = [it for it in new]
            step += 1
        return count


