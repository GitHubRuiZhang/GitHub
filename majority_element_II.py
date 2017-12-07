# python3
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.


# My solution
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums) // 3
        out = set()
        for i in range(n, len(nums)):
            if nums[i] == nums[i - n]:
                out.add(nums[i])
        return list(out)



