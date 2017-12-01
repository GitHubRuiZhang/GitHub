# python3
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


# My solution
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def search(nums):
            pre = None
            if len(nums) == 1:
                return [[nums[0]]]
            out = []
            for i in range(len(nums)):
                if nums[i] != pre:
                    cur = search(nums[:i] + nums[i + 1:])
                    for it in cur:
                        out.append([nums[i]] + it)
                    pre = nums[i]

            return out

        return search(nums)


