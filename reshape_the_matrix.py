# python3
# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different
# size but keep its original data.

# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the
# row number and column number of the wanted reshaped matrix, respectively.

# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order
# as they were.

# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
# Otherwise, output the original matrix.

# Example:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]

# Example:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
#  [3,4]]
# There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

# My solution
# It is slow due to the fact that I have to append every element twice
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums

        nums_one = []
        for i in range(len(nums)):
            nums_one.extend(nums[i])
        # This can be simplified as
        # nume_one = [val for row in nums for val in row]

        new_nums = [[False for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                new_nums[i][j] = nums_one.pop(0)

        return new_nums

# Better solution
# list = [1, 2, 3]
# dictionary = {1: "one", 2: "two", 3: "three"}
# tuple = (1, 2, 3)
# set = {1, 2, 3}

# next(iterator[, default])
# Retrieve the next item from the iterator by calling its next() method.
# If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums

        vals = (val for row in nums for val in row)
        return [[vals.next() for cn in range(c)] for rn in range(r)]