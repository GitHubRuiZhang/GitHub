# python3
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]


# My solution
class Solution(object):
    def test(self, s):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = {s}
        while True:
            cur = filter(self.test, res)
            if cur:
                return cur
            res = {it[:i] + it[i + 1:] for it in res for i in range(len(it))}
