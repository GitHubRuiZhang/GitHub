# python3
# Convert a non-negative integer to its english words representation.
# Given input is guaranteed to be less than 231 - 1.

# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


# Solution
class Solution(object):
    def __init__(self):
        self.oneten = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        self.tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    def words(self, n):
        if n < 20:
            return self.oneten[
                   n - 1:n]  # cannot use [self.oneten[n-1]], the boundary case is when n == 20, will return 'Nineteen'
        if n < 100:
            return [self.tens[n / 10 - 2]] + self.words(n % 10)
        if n < 1000:
            return [self.oneten[n / 100 - 1]] + ['Hundred'] + self.words(n % 100)
        res = ['Thousand', 'Million', 'Billion']
        for i in range(1, 4):
            if n < 1000 ** (i + 1):
                return self.words(n / 1000 ** i) + [res[i - 1]] + self.words(n % 1000 ** i)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        out = self.words(num)
        return " ".join(out)



