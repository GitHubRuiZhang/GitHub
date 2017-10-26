# python3
# Determine whether an integer is a palindrome. Do this without extra space.


# My solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x >= 0 and str(x) == str(x)[::-1]
