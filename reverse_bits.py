# python3
# Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).

# Follow up:
# If this function is called many times, how would you optimize it?


# My solution
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n_bit = '{0:032b}'.format(n)
        n_bit = n_bit[::-1]
        return int(n_bit, 2)
