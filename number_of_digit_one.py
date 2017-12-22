# python3
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.


# Solution
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while i <= n:
            cur = i * 10
            count += (n / cur) * i + min(max(n % cur - i + 1, 0), i)
            i *= 10
        return count
