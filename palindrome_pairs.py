# python3
# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]


# Solution
class Solution(object):
    def check(self, s):
        return s == s[::-1]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = {}
        out = []
        for i in range(len(words)):
            res[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                cur1 = words[i][:j]
                cur2 = words[i][j:]
                if cur1[::-1] in res and res[cur1[::-1]] != i and cur2 == cur2[::-1]:
                    out.append([i, res[cur1[::-1]]])
                if j != 0 and cur2[::-1] in res and res[cur2[::-1]] != i and cur1 == cur1[::-1]:
                    out.append([res[cur2[::-1]], i])

        return out
