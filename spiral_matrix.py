# python3
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


# My solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        row = 0
        column = 0
        row_bound = [0, len(matrix)]
        column_bound = [0, len(matrix[0])]
        direction = 'right'
        out = []
        while len(out) < len(matrix) * len(matrix[0]):
            out.append(matrix[row][column])
            if direction == 'right':
                if column + 1 < column_bound[1]:
                    column += 1
                else:
                    direction = 'down'
                    row += 1
                    column_bound[1] -= 1

            elif direction == 'down':
                if row + 1 < row_bound[1]:
                    row += 1
                else:
                    direction = 'left'
                    column -= 1
                    row_bound[1] -= 1

            elif direction == 'left':
                if column - 1 >= column_bound[0]:
                    column -= 1
                else:
                    direction = 'up'
                    row -= 1
                    column_bound[0] += 1

            elif direction == 'up':
                if row - 1 > row_bound[0]:
                    row -= 1
                else:
                    direction = 'right'
                    column += 1
                    row_bound[0] += 1

        return out






