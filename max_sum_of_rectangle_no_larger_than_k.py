# python3
# Given a non-empty 2D matrix matrix and an integer k,
# find the max sum of a rectangle in the matrix such that its sum is no larger than k.

# Example:
# Given matrix = [
#   [1,  0, 1],
#   [0, -2, 3]
# ]
# k = 2
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?


# Solution
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if matrix == [] or matrix == [[]]:
            return 0
        m = max(len(matrix), len(matrix[0]))
        n = min(len(matrix), len(matrix[0]))
        out = None
        for i in range(n):
            res = [0 for _ in range(m)]
            for j in range(i, n):
                cur = []
                num = 0
                for it in range(m):
                    if len(matrix) > len(matrix[0]):
                        res[it] += matrix[it][j]
                    else:
                        res[it] += matrix[j][it]
                    num += res[it]
                    if num <= k:
                        out = max(out, num)
                    index = bisect.bisect_left(cur, num-k)
                    if index != len(cur):
                        out = max(out, num-cur[index])
                    bisect.insort(cur, num)
        return out