# python3
# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2.

# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


# My solution
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        out = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res = int(num1[i]) * int(num2[j])
                out[i + j + 1] += res
                k = 1
                while out[i + j + k] > 9:
                    out[i + j + k - 1] += (out[i + j + k] // 10)
                    out[i + j + k] %= 10
                    k -= 1

        return str(int(''.join(map(str, out))))

        return str(int(num1) * int(num2))
