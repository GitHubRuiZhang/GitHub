# python3
# Given a string representing an expression of fraction addition and subtraction,
# you need to return the calculation result in string format.
# The final result should be irreducible fraction.
# If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1.
# So in this case, 2 should be converted to 2/1.

# Example 1:
# Input:"-1/2+1/2"
# Output: "0/1"
# Example 2:
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:
# Input:"1/3-1/2"
# Output: "-1/6"
# Example 4:
# Input:"5/3+1/3"
# Output: "2/1"
# Note:
# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has format ±numerator/denominator.
# If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions,
# where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1,
# it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.


# My solution
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x

        def find(expression, i):
            while i < len(expression):
                if expression[i] == '+' or expression[i] == '-':
                    return i
                i += 1
            return i + 1

        if expression[0] == '-':
            index = find(expression, 1)
            num = expression[1:index].split('/')
            out = [-int(num[0]), int(num[1])]
        else:
            index = find(expression, 0)
            num = expression[0:index].split('/')
            out = [int(num[0]), int(num[1])]

        while index < len(expression):
            print(index, out)
            if expression[index] == '+':
                old_index = index
                index = find(expression, index + 1)
                num = expression[old_index + 1:index].split('/')
                out = [out[0] * int(num[1]) + int(num[0]) * out[1], int(num[1]) * out[1]]
            elif expression[index] == '-':
                old_index = index
                index = find(expression, index + 1)
                num = expression[old_index + 1:index].split('/')
                out = [out[0] * int(num[1]) - int(num[0]) * out[1], int(num[1]) * out[1]]

        div = gcd(abs(out[0]), abs(out[1]))
        out = [str(out[0] / div), str(out[1] / div)]
        return '/'.join(out)


