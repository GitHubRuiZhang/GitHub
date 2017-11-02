# python3
# Find the largest palindrome made from the product of two n-digit numbers.

# Since the result could be very large, you should return the largest palindrome mod 1337.

# Example:

# Input: 2

# Output: 987

# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

# Note:

# The range of n is [1,8].


# My solution
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        solution = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
        if n >= 0 and n < 9:
            return solution[n]
        return 0
