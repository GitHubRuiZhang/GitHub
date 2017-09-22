# python3
# output an integer's complement number
# the complement strategy is to flip the bits of its binary representation

# Example
# Input: 5
# Output: 2
# Explanation: 5 -> 101, 2 -> 010

# My solution, slow
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = format(num,'b')
        return int(''.join('0' if item is '1' else '1' for item in bin_num),2)


# Fast solution
# bitwise operator
# x << y returns x with the bits shifted to the left by y places
# ^ is bitwise XOR operator
# not sure what is the meaning of it
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
