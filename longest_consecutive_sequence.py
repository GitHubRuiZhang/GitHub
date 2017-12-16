# python3
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.


# My solution
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        out = 0
        cur = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            out = max(out, cur)
        return out


