# python3
# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
# The integer division should truncate toward zero.

# You may assume that the given expression is always valid.

# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.


# My solution
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        all_nums = []
        all_operations = []
        times = False
        divides = False
        pre = ''
        for i in range(len(s)):
            if s[i] in digits:
                pre += s[i]
            elif s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                all_nums.append(int(pre))
                all_operations.append(s[i])
                pre = ''
        all_nums.append(int(pre))
        print(all_nums, all_operations)
        i = 0
        while i < len(all_operations):
            if all_operations[i] == '*':
                all_operations.pop(i)
                left = all_nums.pop(i)
                right = all_nums.pop(i)
                all_nums.insert(i, left * right)
            elif all_operations[i] == '/':
                all_operations.pop(i)
                left = all_nums.pop(i)
                right = all_nums.pop(i)
                all_nums.insert(i, left / right)
            else:
                i += 1
        i = 1
        out = all_nums[0]
        while i < len(all_nums):
            if all_operations[i - 1] == '+':
                out += all_nums[i]
            else:
                out -= all_nums[i]

            i += 1
        return out







