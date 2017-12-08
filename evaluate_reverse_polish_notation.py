# python3
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


# My solution
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num1 + num2)
            elif tokens[i] == '-':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2 - num1)
            elif tokens[i] == '*':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2 * num1)
            elif tokens[i] == '/':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(float(num2) / num1))
            else:
                nums.append(int(tokens[i]))

        return nums[0]
