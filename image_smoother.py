# python3
# Given a 2D integer matrix M representing the gray scale of an image,
# you need to design a smoother to make the gray scale of each cell
# becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.
# If a cell has less than 8 surrounding cells, then use as many as you can.

# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].


# My solution
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if M == [[]]:
            return M
        output = [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 1
                if i > 0 and j > 0:
                    output[i][j] += (M[i - 1][j] + M[i - 1][j - 1] + M[i][j - 1])
                    count += 3
                elif i > 0:
                    output[i][j] += (M[i - 1][j])
                    count += 1
                elif j > 0:
                    output[i][j] += (M[i][j - 1])
                    count += 1

                if i < len(M) - 1 and j < len(M[0]) - 1:
                    output[i][j] += (M[i + 1][j] + M[i + 1][j + 1] + M[i][j + 1])
                    count += 3
                elif i < len(M) - 1:
                    output[i][j] += M[i + 1][j]
                    count += 1
                elif j < len(M[0]) - 1:
                    output[i][j] += M[i][j + 1]
                    count += 1

                if i > 0 and j < len(M[0]) - 1:
                    output[i][j] += M[i - 1][j + 1]
                    count += 1

                if i < len(M) - 1 and j > 0:
                    output[i][j] += M[i + 1][j - 1]
                    count += 1

                output[i][j] //= count

        return output