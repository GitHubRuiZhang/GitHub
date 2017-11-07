# python3
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Now your job is to find the total Hamming distance between all pairs of the given numbers.

# Example:
# Input: 4, 14, 2

# Output: 6

# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

# Note:
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4.


# My solution, slow
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def hammingDistance(a, b):
            return bin(a ^ b).count('1')

        out = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                out += hammingDistance(nums[i], nums[j])

        return out


# My solution
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_nums = []
        for i in range(len(nums)):
            bit_nums.append('{0:032b}'.format(nums[i]))

        zero_ones = [[0, 0] for _ in range(32)]
        for i in range(32):
            for num in bit_nums:
                if num[i] == '0':
                    zero_ones[i][0] += 1
                else:
                    zero_ones[i][1] += 1

        return sum(x * y for x, y in zero_ones)
