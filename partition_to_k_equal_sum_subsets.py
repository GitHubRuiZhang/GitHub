# python3
# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into
# k non-empty subsets whose sums are all equal.

# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

# Note:

# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.


# My solution
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort()
        if len(nums) < k or nums[-1] > sum(nums) // k or sum(nums) % k != 0:
            return False

        out = [[] for _ in range(k)]

        def search(nums_res, out_res, target):
            if nums_res == []:
                for i in range(len(out_res)):
                    if sum(out_res[i]) != target:
                        return False
                return True
            while nums_res:
                cur = nums_res.pop()
                for i in range(len(out_res)):
                    if out_res[i] != [] and sum(out_res[i]) + cur <= target:
                        out_res[i].append(cur)
                        if search(nums_res, out_res, target):
                            return True
                        out_res[i].pop()
                    elif out_res[i] == []:
                        out_res[i].append(cur)
                        if search(nums_res, out_res, target):
                            return True
                        out_res[i].pop()
                        break
                nums_res.append(cur)
                return False

        return search(nums, out, sum(nums) // k)



