# python3
# Given an integer, write a function to determine if it is a power of two.


# My solution
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        return n&(n-1) == 0