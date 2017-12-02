# python3
# Given a matrix consists of 0 and 1,
# find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.
# Example 1:
# Input:

# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:

# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


# My solution
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        out = [[float('inf') for j in range(len(matrix[0]))] for i in range(len(matrix))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        nodes = []

        def search(i, j):
            for it in directions:
                x = i - it[0]
                y = j - it[1]
                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
                    if out[x][y] > out[i][j] + 1:
                        out[x][y] = out[i][j] + 1
                        nodes.append((x, y))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    nodes.append((i, j))
                    out[i][j] = 0

        while nodes:
            cur = nodes.pop(0)
            search(cur[0], cur[1])

        return out


