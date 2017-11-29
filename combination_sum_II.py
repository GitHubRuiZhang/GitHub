# python3
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]


# My solution
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out = []

        def search(nums, pre, target):
            if target == 0:
                if pre not in out:
                    out.append(pre)
                return True
            elif target < 0 or sum(nums) < target:
                return False

            for i in range(len(nums)):
                if nums[i] > target:
                    continue
                else:
                    search(nums[i + 1:], pre + [nums[i]], target - nums[i])

        candidates.sort()
        candidates[::-1]
        search(candidates, [], target)
        return out

