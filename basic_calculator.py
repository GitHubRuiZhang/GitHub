# python3
# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .

# You may assume that the given expression is always valid.

# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# Note: Do not use the eval built-in library function.


# My solution
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = []
        sign = 1
        cur = 0
        num = 0
        for i in range(len(s)):
            if s[i] in digits:
                num = 10 * num + int(s[i])
            elif s[i] == '+' or s[i] == '-':
                cur += sign * num
                num = 0
                if s[i] == '+':
                    sign = 1
                else:
                    sign = -1
            elif s[i] == "(":
                res.append(cur)
                res.append(sign)
                sign = 1
                cur = 0
            elif s[i] == ')':
                cur += sign * num
                cur *= res.pop()
                cur += res.pop()
                num = 0
        return cur + num * sign



