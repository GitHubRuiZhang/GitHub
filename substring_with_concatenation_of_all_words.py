# python3
# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words
# exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter).


# My solution
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words.sort()
        n = len(words)
        m = len(words[0])
        out = []
        for i in range(len(s) - m * n + 1):
            if s[i:i + m] in words:
                cur = []
                for j in range(n):
                    cur.append(s[(i + j * m):(i + (j + 1) * m)])
                cur.sort()
                if cur == words:
                    out.append(i)
        return out






