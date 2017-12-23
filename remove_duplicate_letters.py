# python3
# Given a string which contains only lowercase letters,
# remove duplicate letters so that every letter appear once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Example:
# Given "bcabc"
# Return "abc"

# Given "cbacdcbc"
# Return "acdb"


# Solution
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        for it in sorted(set(s)):
            pre = s[s.index(it):]
            if set(pre) == set(s):
                return it + self.removeDuplicateLetters(pre.replace(it, ''))
        return ''
