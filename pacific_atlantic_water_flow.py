# python3
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
# the "Pacific ocean" touches the left and top edges of the matrix
# and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height
# equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


# My solution
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix == []:
            return []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        atlantic = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]

        def dfs(i, j, visited):
            visited[i][j] = True
            for it in directions:
                x = i + it[0]
                y = j + it[1]
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or visited[x][y] or matrix[i][j] > \
                        matrix[x][y]:
                    continue
                else:
                    dfs(x, y, visited)

        for i in range(len(matrix)):
            dfs(i, 0, pacific)
            dfs(i, len(matrix[0]) - 1, atlantic)

        for j in range(len(matrix[0])):
            dfs(0, j, pacific)
            dfs(len(matrix) - 1, j, atlantic)

        out = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific[i][j] and atlantic[i][j]:
                    out.append([i, j])
        return out












