# python3
# Given an array of integers, every element appears three times except for one, which appears exactly once.
# Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


# My solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) < 3:
            return nums.pop()
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
        if nums[0] != nums[1]:
            return nums[0]
        else:
            return nums[-1]

