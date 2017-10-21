# python3
# Given an integer, write a function to determine if it is a power of three.


# My solution
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return 1162261467%n == 0