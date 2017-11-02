# python3
# Given two strings representing two complex numbers.

# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

# Note:

# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and b will both belong to the
# range of [-100, 100]. And the output should be also in this form.


# My solution
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list = a.split('+')
        a_re = int(a_list[0])
        a_co = int(a_list[1][:len(a_list[1]) - 1])
        b_list = b.split('+')
        b_re = int(b_list[0])
        b_co = int(b_list[1][:len(b_list[1]) - 1])
        out_re = a_re * b_re - a_co * b_co
        out_co = a_re * b_co + a_co * b_re
        return str(out_re) + '+' + str(out_co) + 'i'


