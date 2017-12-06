# python3
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.


# My solution
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # fast
        if len(nums) == 1:
            return True
        possible = [False for _ in range(len(nums))]
        possible[0] = True
        trueposition = 0
        for i in range(len(nums)):
            if possible[i] == False:
                return False
            if i + nums[i] > trueposition:
                for j in range(nums[i]):
                    if i + j + 1 < len(nums):
                        possible[i + j + 1] = True
                        trueposition = i + j + 1
            if possible[-1] == True:
                return True
        return possible[-1]

        # slow
        if len(nums) == 1:
            return True
        possible = [False for _ in range(len(nums))]
        possible[0] = True
        for i in range(len(nums)):
            if possible[i] == False:
                return False
            for j in range(nums[i]):
                if i + j + 1 < len(nums):
                    possible[i + j + 1] = True
            if possible[-1] == True:
                return True
        return possible[-1]


