# python3
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.


# My solution
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        right = 0
        left = 0
        res = 0
        if sum(nums) < s:
            return 0
        out = len(nums)
        while right < len(nums):
            if res + nums[right] >= s:
                out = min(out, right - left + 1)
                res -= nums[left]
                left += 1
            else:
                res += nums[right]
                right += 1

        return out

