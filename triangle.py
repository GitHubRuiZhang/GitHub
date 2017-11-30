# python3
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.


# My solution
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = [[False for i in range(len(triangle[j]))] for j in range(len(triangle))]

        def search(triangle, r, c):
            if r >= len(triangle) or c >= len(triangle):
                return False
            elif r == len(triangle) - 1:
                return triangle[r][c]
            if res[r][c] != False:
                return res[r][c]
            left = search(triangle, r + 1, c)
            right = search(triangle, r + 1, c + 1)
            res[r][c] = triangle[r][c] + min(left, right)
            return res[r][c]

        return search(triangle, 0, 0)

