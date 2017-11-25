# python3
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.


# My solution
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = set([])
        c = set([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)

        for it in r:
            matrix[it] = [0 for i in range(len(matrix[0]))]

        for it in c:
            for i in range(len(matrix)):
                matrix[i][it] = 0

        return

