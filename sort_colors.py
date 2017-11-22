# python3
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.


# My solution
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                n -= 1
            else:
                i += 1

        return




