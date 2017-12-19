# python3
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.


# My solution
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == [] or matrix == [[]]:
            return 0
        out = 0
        height = [0 for _ in range(len(matrix[0]) + 1)]
        for r in matrix:
            height = [height[j] + 1 if r[j] == '1' else 0 for j in range(len(matrix[0]))]
            height.append(0)
            res = [-1]
            for i in range(len(matrix[0]) + 1):
                while height[i] < height[res[-1]]:
                    out = max(out, (height[res.pop()]) * (i - res[-1] - 1))
                res.append(i)
        return out

