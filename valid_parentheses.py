# python3
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


# My solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair_item = []
        for item in s:
            if item == '(' or item == '{' or item == '[':
                pair_item.append(item)
            elif pair_item == []:
                return False
            elif item == ')' and pair_item[-1] != '(':
                return False
            elif item == '}' and pair_item[-1] != '{':
                return False
            elif item == ']' and pair_item[-1] != '[':
                return False
            elif item == ')' and pair_item[-1] == '(':
                del pair_item[-1]
                print('1')
            elif item == '}' and pair_item[-1] == '{':
                del pair_item[-1]
            elif item == ']' and pair_item[-1] == '[':
                del pair_item[-1]

        return len(pair_item) == 0
