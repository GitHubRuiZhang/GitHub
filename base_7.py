# python3
# Given an integer, return its base 7 string representation.

# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"


# My solution
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        output = ''
        sign = ''
        if num < 0:
            sign = '-'
            num = abs(num)
        while num != 0:
            output = str(num % 7) + output
            num //= 7
        return sign + output
