# python3
# Find the length of the longest substring T of a given string (consists of lowercase letters only)
# such that every character in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3

# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input:
# s = "ababbc", k = 2

# Output:
# 5

# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


# My solution
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Not mine, I counldn't write a better solution
        if len(s) < k:
            return 0
        min_letter = min(set(s), key=s.count)
        if s.count(min_letter) >= k:
            return len(s)
        return max(self.longestSubstring(sub_string, k) for sub_string in s.split(min_letter))
