# python3
# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.


# My solution
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == -2147483648 and divisor == -1):
            return 2147483647

        i = 0
        Sign = False
        if dividend < 0 and divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif dividend < 0:
            Sign = True
            dividend = abs(dividend)
        elif divisor < 0:
            Sign = True
            divisor = abs(divisor)

        out = 0
        while dividend >= divisor:
            res = divisor
            i = 1
            while dividend >= res:
                dividend -= res
                out += i
                res <<= 1
                i <<= 1

        if Sign:
            out = - out
        return out
