# python3
# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1:

# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].

# Example 2:

# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


# Solution
class Solution(object):
    def search(self, matrix, i, j):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if not self.res[i][j]:
            cur = matrix[i][j]
            self.res[i][j] = 1
            for it in directions:
                if i + it[0] >= 0 and j + it[1] >= 0 and i + it[0] < len(matrix) and j + it[1] < len(
                        matrix[0]) and cur > matrix[i + it[0]][j + it[1]]:
                    self.res[i][j] = max(self.res[i][j], 1 + self.search(matrix, i + it[0], j + it[1]))
        return self.res[i][j]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix == [] or matrix == [[]]:
            return 0
        self.res = [[0 for j in range(len(matrix[0]))] for j in range(len(matrix))]
        return max(self.search(matrix, i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))
