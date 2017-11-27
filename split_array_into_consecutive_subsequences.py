# python3
# You are given an integer array sorted in ascending order (may contain duplicates),
# you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers.
# Return whether you can make such a split.

# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False
# Note:
# The length of the input is in range of [1, 10000]


# My solution
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = collections.Counter(nums)
        end = collections.Counter()
        for it in nums:
            if res[it] < 1:
                continue
            res[it] -= 1
            if end[it - 1] > 0:
                # join pre
                end[it - 1] -= 1
                end[it] += 1
            elif res[it + 1] > 0 and res[it + 2] > 0:
                # start new
                res[it + 1] -= 1
                res[it + 2] -= 1
                end[it + 2] += 1
            else:
                # couldnt join or start
                return False
        return True






