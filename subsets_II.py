# python3
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


# My solution
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        out = [[]]
        for i in range(len(nums)):
            for j in range(len(out)):
                cur = out[j] + [nums[i]]
                if cur not in out:
                    out.append(out[j] + [nums[i]])

        return out

