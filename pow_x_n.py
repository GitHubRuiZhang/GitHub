# python3
# Implement pow(x, n).


# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100


# My solution
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / x * self.myPow(1 / x, -(n + 1))
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        if n % 2 == 0:
            return self.myPow(self.myPow(x, n // 2), 2)
        else:
            return x * self.myPow(self.myPow(x, n // 2), 2)

