# python3
# Implement int sqrt(int x).

# Compute and return the square root of x.


# My solution
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r