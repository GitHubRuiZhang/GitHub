# python3
# Given a matrix of M x N elements (M rows, N columns),
# return all elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:

# Note:
# The total number of elements of the given matrix will not exceed 10,000.


# My solution
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        i, j = 0, 0
        direction_up = True
        out = []
        x_length = len(matrix)
        y_length = len(matrix[0])
        while len(out) != x_length * y_length:
            out.append(matrix[i][j])
            if direction_up and j == y_length - 1:
                i += 1
                direction_up = False
            elif direction_up and i == 0:
                j += 1
                direction_up = False
            elif direction_up:
                i -= 1
                j += 1
            elif i == x_length - 1:
                j += 1
                direction_up = True
            elif j == 0:
                i += 1
                direction_up = True
            else:
                j -= 1
                i += 1

        return out

