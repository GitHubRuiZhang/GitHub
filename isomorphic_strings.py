# python3
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

# Note:
# You may assume both s and t have the same length.


# My solution
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        item_s = {}
        item_t = {}
        count = 0
        for i in range(len(s)):
            if s[i] in item_s and t[i] in item_t:
                if item_s[s[i]] != item_t[t[i]]:
                    return False
            elif s[i] not in item_s and t[i] not in item_t:
                item_s[s[i]] = count
                item_t[t[i]] = count
                count += 1
            else:
                return False

        return True
