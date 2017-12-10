# python3
# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.


# My solution
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        out = 1
        j = 1
        possible = s[0]
        while j < len(s):
            if s[j] not in possible:
                possible += s[j]
                out = max(out, len(possible))
            else:
                for i in range(len(possible)):
                    if possible[i] == s[j]:
                        break
                possible = possible[i + 1:] + s[j]
            j += 1

        return out








