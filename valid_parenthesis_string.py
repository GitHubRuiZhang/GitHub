# python3
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].


# My solution
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = [0]
        for i in range(len(s)):
            if s[i] == '(':
                for j in range(len(left)):
                    left[j] += 1
            elif s[i] == ')':
                j = 0
                while j < len(left):
                    if left[j] == 0:
                        left.pop(j)
                    else:
                        left[j] -= 1
                        j += 1
                if left == []:
                    return False
            else:
                j = 0
                n = len(left)
                while j < n:
                    left.append(left[j] + 1)
                    if left[j] != 0:
                        left.append(left[j] - 1)
                    j += 1
            left = list(set(left))
        for it in left:
            if it == 0:
                return True
        return False





