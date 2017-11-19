# python3
# Given a set of candidate numbers (C) (without duplicates) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]


# My solution
class Solution(object):
    def __init__(self):
        self.out = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(nums, target, path, pre):
            if target < 0:
                return
            elif target == 0:
                self.out.append(path)
                return
            else:
                res = []
                for i in range(pre, len(nums)):
                    cur = dfs(nums, target - nums[i], path + [nums[i]], i)

        dfs(candidates, target, [], 0)
        return self.out








