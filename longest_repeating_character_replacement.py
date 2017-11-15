# python3
# Given a string that consists of only uppercase English letters,
# you can replace any letter in the string with another letter at most k times.
# Find the length of a longest substring containing all repeating letters
# you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


# My solution
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        win_length = 0
        max_char_count = 0
        counts = {}
        for end in range(len(s)):
            if s[end] in counts:
                counts[s[end]] += 1
            else:
                counts[s[end]] = 1
            if max_char_count < counts[s[end]]:
                max_char_count = counts[s[end]]
            while end - start + 1 - max_char_count > k:
                counts[s[start]] -= 1
                start += 1
            win_length = max(win_length, end - start + 1)
        return win_length


