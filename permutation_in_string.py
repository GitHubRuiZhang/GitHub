# python3
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].


# My solution
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def judge(frequencies, cur_frequencies):
            key1 = sorted(frequencies.keys())
            key2 = sorted(cur_frequencies.keys())
            if len(key1) == len(key2):
                count = 0
                for i in range(len(key1)):
                    if key1[i] == key2[i] and frequencies[key1[i]] == cur_frequencies[key2[i]]:
                        count += 1
                    else:
                        break
                if count == len(key1):
                    return True
            else:
                return False

        if len(s1) > len(s2):
            return False
        frequencies = {}
        cur_frequencies = {}
        for i in range(len(s1)):
            if s1[i] in frequencies:
                frequencies[s1[i]] += 1
            else:
                frequencies[s1[i]] = 1

            if s2[i] in cur_frequencies:
                cur_frequencies[s2[i]] += 1
            else:
                cur_frequencies[s2[i]] = 1

        if judge(frequencies, cur_frequencies):
            return True

        for i in range(len(s1), len(s2)):
            cur = s2[i - len(s1)]
            if cur_frequencies[cur] > 1:
                cur_frequencies[cur] -= 1
            else:
                del cur_frequencies[cur]

            cur = s2[i]
            if cur in cur_frequencies:
                cur_frequencies[cur] += 1
            else:
                cur_frequencies[cur] = 1

            if judge(frequencies, cur_frequencies):
                return True

        return False





