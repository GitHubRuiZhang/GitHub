# python3
# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.


# My solution
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x_str = str(x)[::-1]
            if int(x_str) > 2 ** 31:
                return 0
            else:
                return int(x_str)
        else:
            x_str = str(x)[1:]
            x_str = x_str[::-1]
            if int(x_str) > 2 ** 31:
                return 0
            else:
                return -int(x_str)



