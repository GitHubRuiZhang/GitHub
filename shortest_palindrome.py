# python3
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
# Find and return the shortest palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".


# 
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s + '$' + s[::-1]
        table = [0]
        for i in range(1, len(res)):
            cur = table[i - 1]
            while cur > 0 and res[cur] != res[i]:
                cur = table[cur - 1]
            if res[cur] == res[i]:
                table.append(cur + 1)
            else:
                table.append(cur)
        return s[table[-1]:][::-1] + s


