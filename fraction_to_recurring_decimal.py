# python3
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".


# My solution
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator * denominator < 0:
            sign = '-'
        else:
            sign = ''

        numerator, denominator = abs(numerator), abs(denominator)
        cur = numerator % denominator
        out = [sign + str(numerator // denominator), '.']
        res = []
        while cur not in res:
            res.append(cur)
            out.append(str(cur * 10 // denominator))
            cur = (cur * 10) % denominator

        idx = res.index(cur)
        out.insert(idx + 2, '(')
        out.append(')')
        return ''.join(out).replace('(0)', '').rstrip('.')


