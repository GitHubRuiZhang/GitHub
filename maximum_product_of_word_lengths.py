# python3
# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words
# do not share common letters. You may assume that each word will contain only lower case letters.
# If no such two words exist, return 0.

# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".

# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".

# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.


# My solution
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        if len(words) < 2:
            return 0
        out = 0
        set_words = []
        for i in range(len(words)):
            set_words.append(set(words[i]))
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(set_words[i].intersection(set_words[j])) == 0:
                    out = max(out, len(words[i]) * len(words[j]))

        return out

