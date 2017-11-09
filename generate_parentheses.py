# python3
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


# My solution, i dont understand now
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        left, right, out = n, n, []
        self.search(left, right, out, "")
        return out

    def search(self, left, right, out, string):
        if right < left:
            return
        if left == 0 and right == 0:
            out.append(string)
            return
        if left > 0:
            self.search(left - 1, right, out, string + "(")
        if right > 0:
            self.search(left, right - 1, out, string + ")")


