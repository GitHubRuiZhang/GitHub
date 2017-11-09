# python3
# Given a positive integer n, break it into the sum of at least two positive integers
# and maximize the product of those integers. Return the maximum product you can get.

# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

# Note: You may assume that n is not less than 2 and not larger than 58.


# My solution
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        out = 1
        while n > 4:
            out *= 3
            n -= 3
        else:
            out *= n
        return out

