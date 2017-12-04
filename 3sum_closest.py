# python3
# Given an array S of n integers,
# find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


# My solution
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        out = float('inf')
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if abs(res - target) < abs(out - target):
                    out = res
                if res - target > 0:
                    r -= 1
                elif res - target == 0:
                    return target
                else:
                    l += 1

        return out

