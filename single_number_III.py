# python3
# Given an array of numbers nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that appear only once.

# For example:

# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


# My solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = set()
        for i in range(len(nums)):
            if nums[i] not in out:
                out.add(nums[i])
            else:
                out.remove(nums[i])

        return list(out)
