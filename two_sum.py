# python3
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# My solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        possible_out = {}
        for i in range(len(nums)):
            if target - nums[i] in possible_out:
                return [possible_out[target - nums[i]], i]
            else:
                possible_out[nums[i]] = i
        return False

