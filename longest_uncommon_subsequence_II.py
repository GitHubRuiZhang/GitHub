# python3
# Given a list of strings, you need to find the longest uncommon subsequence among them.
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings
# and this subsequence should not be any subsequence of the other strings.

# A subsequence is a sequence that can be derived from one sequence by deleting some characters
# without changing the order of the remaining elements. Trivially,
# any string is a subsequence of itself and an empty string is a subsequence of any string.

# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.

# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3
# Note:

# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].


# My solution
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def two_strs(a, b):
            # return true if a is a substring of b
            i = 0
            for it in b:
                if i < len(a) and a[i] == it:
                    i += 1

            return i == len(a)

        strs = sorted(strs, key=len, reverse=True)
        for i in range(len(strs)):
            judge = False
            for j in range(len(strs)):
                if j != i and two_strs(strs[i], strs[j]):
                    judge = True
                    break
            if not judge:
                return len(strs[i])

        return -1

