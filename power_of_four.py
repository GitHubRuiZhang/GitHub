# python3
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example:
# Given num = 16, return true. Given num = 5, return false.

# Follow up: Could you solve it without loops/recursion?


# My solution
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num > 1:
            if num % 4 != 0:
                return False
            else:
                num /= 4

        return True


# Solution without loop:
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0) and (num & (num - 1) == 0) and (num & 1431655765 == num)
