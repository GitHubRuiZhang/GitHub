# python3
# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
# then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.


# My solution
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words.sort()
        all_word_map = {}
        all_word_count = []
        for word in words:
            if word not in all_word_map:
                all_word_map[word] = len(all_word_count)
                all_word_count.append([word, 1])
            else:
                all_word_count[all_word_map[word]][1] += 1

        all_word_count = sorted(all_word_count, key=lambda x: x[1])
        out = []
        pre_count = 0
        pre_index = None
        i = 0
        while len(all_word_count) > 0:
            cur = all_word_count.pop()
            if cur[1] != pre_count:
                pre_count = cur[1]
                pre_index = len(out)
                out.append(cur[0])
            else:
                out.insert(pre_index, cur[0])

        return out[:k]



