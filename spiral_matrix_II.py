# python3
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


# My solution
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        out = [[False for i in range(n)] for j in range(n)]
        out[0] = [i + 1 for i in range(n)]
        cur = n + 1
        for i in range(n - 1):
            out[i + 1][-1] = cur
            cur += 1
        for i in range(n - 1):
            out[-1][n - i - 2] = cur
            cur += 1
        row = False
        i = n - 2
        j = 0
        while cur <= n ** 2:
            out[i][j] = cur
            cur += 1
            if not row:
                if out[i - 1][j] is not False and out[i + 1][j] is not False:
                    row = True
                    if out[i][j + 1] is False:
                        j += 1
                    else:
                        j -= 1
                elif out[i - 1][j] is False:
                    i -= 1
                else:
                    i += 1
            else:
                if out[i][j - 1] is not False and out[i][j + 1] is not False:
                    row = False
                    if out[i + 1][j] is False:
                        i += 1
                    else:
                        i -= 1
                elif out[i][j - 1] is False:
                    j -= 1
                else:
                    j += 1

        return out








