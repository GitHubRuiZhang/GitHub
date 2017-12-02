# python3
# Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz",
# so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

# Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s.
# In particular, your input is the string p and you need to output the number of different non-empty
# substrings of p in the string s.

# Note: p consists of only lowercase English letters and the size of p might be over 10000.

# Example 1:
# Input: "a"
# Output: 1

# Explanation: Only the substring "a" of string "a" is in the string s.
# Example 2:
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string s.
# Example 3:
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.


# My solution
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = [0 for _ in range(26)]
        cur = 1
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i - 1]) - ord(p[i]) == 25):
                cur += 1
            else:
                cur = 1

            count[ord(p[i]) - ord('a')] = max(count[ord(p[i]) - ord('a')], cur)

        return sum(count)


