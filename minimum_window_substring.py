# python3
# Given a string S and a string T,
# find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".

# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.


# My solution

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = {}
        for i in range(len(t)):
            if t[i] in res:
                res[t[i]] += 1
            else:
                res[t[i]] = 1
        start, end, count = 0, 0, len(t)
        distance = float('inf')
        head = 0
        while end < len(s):
            if s[end] in res:
                res[s[end]] -= 1
                if res[s[end]] >= 0:
                    count -= 1
            end += 1
            while count == 0:
                if end - start < distance:
                    distance = end - start
                    head = start
                if s[start] in res:
                    res[s[start]] += 1
                    if res[s[start]] > 0:
                        count += 1
                start += 1
        if distance > len(s) + 1:
            return ""
        else:
            return s[head:(head + distance)]



