# python3
# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.


# My solution
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        nums = [it if (it >= 0 and it < n) else 0 for it in nums]
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return n


