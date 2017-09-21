# python3

# 2n integers
# (a1,b1), ..., (an,bn)
# make the sum of min(a_i,b_i) as large as possible

# Example
# Input: [1,4,3,2]
# Output: 4
# Explanation:
# (1,2), (3,4) -> 1 + 3 = 4

# My solution:
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[0::2])

# with '0', it is slower

# Better solution:
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])