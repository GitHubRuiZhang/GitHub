# python3
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to
# the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].

# Follow up:
# Could you solve it with constant space complexity? (Note:
# The output array does not count as extra space for the purpose of space complexity analysis.)


# My solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [1 for _ in range(len(nums))]
        increase = 1
        decrease = 1
        for i in range(len(nums)):
            out[i] *= increase
            out[-i - 1] *= decrease
            increase *= nums[i]
            decrease *= nums[-i - 1]

        return out
