# python3
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# My solution
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        pre = None  # remove duplicates
        out = []
        for i in range(len(nums)):
            if pre == nums[i]:
                continue
            pre = nums[i]
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                res = nums[l] + nums[r]
                if res < target:
                    l += 1
                elif res == target:
                    out.append([nums[i], nums[l], nums[r]])
                    lpre = nums[l]
                    while l < r and nums[l] == lpre:
                        l += 1
                    rpre = nums[r]
                    while l < r and nums[r] == rpre:
                        r -= 1
                else:
                    r -= 1
        return out

        # Naive
        nums.sort()
        if len(nums) < 3:
            return []
        out = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in out:
                        out.append([nums[i], nums[j], nums[k]])
                    elif nums[i] + nums[j] + nums[k] > 0:
                        break

        return out
