# python3
# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal,
# where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

# You may assume the array's length is at most 10,000.

# Example:
# Input:
# [1,2,3]

# Output:
# 2

# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):

# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]


# My solution
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = sorted(nums)[len(nums) // 2]
        count = 0
        for num in nums:
            count += abs(num - mid)

        return count