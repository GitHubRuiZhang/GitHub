# python3
# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?


# My solution: Clearly I used extra memory
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = set()
        for i in range(len(nums)):
            if nums[i] not in elements:
                elements.add(nums[i])
            else:
                elements.remove(nums[i])

        return elements.pop()


# Better solution
# ^ is Binary XOR
# Example:
# a = 60         60 = 0011 1100
# b = 13         13 = 0000 1101
# c = a ^ b      49 = 0011 0001
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        retval = 0
        for i in nums:
            retval = retval ^ i

        return retval