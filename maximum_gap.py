# python3
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

# Try to solve it in linear time/space.

# Return 0 if the array contains less than 2 elements.

# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


# My solution
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        out = 0
        for i in range(1, len(nums)):
            out = max(out, nums[i] - nums[i - 1])
        return out

