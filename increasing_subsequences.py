# python3
# Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
# and the length of an increasing subsequence should be at least 2 .

# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates,
# and two equal integers should also be considered as a special case of increasing sequence.


# My solution
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        out = set()
        pre = None
        for i in range(len(nums)):
            new_out = set()
            while out:
                it = out.pop()
                if it[-1] <= nums[i]:
                    cur = it + (nums[i],)
                    if cur not in new_out:
                        new_out.add(cur)
                new_out.add(it)
            new_out.add((nums[i],))
            out = new_out

        return [it for it in out if len(it) > 1]









