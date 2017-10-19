# python3
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?


# My solution
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
