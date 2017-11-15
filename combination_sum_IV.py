# python3
# Given an integer array with all positive numbers and no duplicates,
# find the number of possible combinations that add up to a positive integer target.

# Example:

# nums = [1, 2, 3]
# target = 4

# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)

# Note that different sequences are counted as different combinations.

# Therefore the output is 7.


# My solution
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = [0 for _ in range(target + 1)]
        for i in range(1, target + 1):
            count = 0
            for j in range(len(nums)):
                if nums[j] < i:
                    count += res[i - nums[j]]
                elif nums[j] == i:
                    count += 1
                else:
                    break
            res[i] = count

        return res[-1]

