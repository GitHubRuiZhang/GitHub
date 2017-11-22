# python3
# Solve a given equation and return the value of x in the form of string "x=#value".
# The equation contains only '+', '-' operation, the variable x and its coefficient.

# If there is no solution for the equation, return "No solution".

# If there are infinite solutions for the equation, return "Infinite solutions".

# If there is exactly one solution for the equation, we ensure that the value of x is an integer.

# Example 1:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:
# Input: "x=x"
# Output: "Infinite solutions"
# Example 3:
# Input: "2x=x"
# Output: "x=0"
# Example 4:
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
# Example 5:
# Input: "x=x+2"
# Output: "No solution"


# My solution
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        eq = equation.split('=')
        left = eq[0]
        right = eq[1]
        x_count = 0
        value = 0
        pre_operation = None
        num = ''
        for s in left:
            if s == 'x' and num == '':
                if pre_operation == '-':
                    x_count -= 1
                else:
                    x_count += 1
            elif s == 'x':
                if pre_operation == '-':
                    x_count -= int(num)
                else:
                    x_count += int(num)
                num = ''
            elif (s == '+' or s == '-') and num == '':
                pre_operation = s
            elif s == '+' or s == '-':
                if pre_operation == '-':
                    value -= int(num)
                else:
                    value += int(num)
                num = ''
                pre_operation = s
            else:
                num += s
            print(s, num, x_count, value)
        if num != '':
            if pre_operation == '-':
                value -= int(num)
            else:
                value += int(num)
        num = ''
        pre_operation = None
        for s in right:
            if s == 'x' and num == '':
                if pre_operation == '-':
                    x_count += 1
                else:
                    x_count -= 1
            elif s == 'x':
                if pre_operation == '-':
                    x_count += int(num)
                else:
                    x_count -= int(num)
                num = ''
            elif (s == '+' or s == '-') and num == '':
                pre_operation = s
            elif s == '+' or s == '-':
                if pre_operation == '-':
                    value += int(num)
                else:
                    value -= int(num)
                num = ''
                pre_operation = s
            else:
                num += s
            print(s, s is 'x', s == 'x', x_count, value)

        if num != '':
            if pre_operation == '-':
                value += int(num)
            else:
                value -= int(num)
            num = ''
        if x_count is 0 and value is 0:
            return "Infinite solutions"
        elif x_count is 0:
            return "No solution"
        return 'x=' + str(-value / x_count)





