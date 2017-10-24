# python3
# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


# My solution
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        out = [[1] for _ in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                out[i].append(out[i - 1][j - 1] + out[i - 1][j])
            out[i].append(1)

        return out
