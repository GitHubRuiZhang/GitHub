# python3
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# My solution, must do in-place operations
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = 0
        i = 0
        while i < len(nums):
            count += 1
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1

            if count > len(nums):
                break
