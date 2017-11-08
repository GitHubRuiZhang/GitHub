# python3
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

# Could you do this in O(n) runtime?

# Example:

# Input: [3, 10, 5, 25, 2, 8]

# Output: 28

# Explanation: The maximum result is 5 ^ 25 = 28.


# My solution, slow O(n^2)
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]^nums[j] > out:
                    out = nums[i]^nums[j]
        return out


# Fast, not quite understand
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        for i in range(32)[::-1]:
            out <<= 1
            prefix = {num >> i for num in nums}
            for p in prefix:
                if out ^ 1 ^ p in prefix:
                    out += 1
                    break

        return out


