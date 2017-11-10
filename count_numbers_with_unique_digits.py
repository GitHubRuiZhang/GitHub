# python3
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100,
# excluding [11,22,33,44,55,66,77,88,99])


# My solution
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        k = 1
        out = 1
        cur = 1
        while k <= n:
            cur *= min(9, 9 - k + 2)
            out += cur
            k += 1
        return out
