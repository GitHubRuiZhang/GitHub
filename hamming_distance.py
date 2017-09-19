# python3

# The Hamming distance between two integers is the number
# of positions at which the corresponding bits are different

# Example
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1 -> (0 0 0 1)
# 4 -> (0 1 0 0)
# Dif:  0 1 0 1


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Solution 1
        # "^" is the bitwise XOR operator
        output = bin(x ^ y).count('1')
        return output
