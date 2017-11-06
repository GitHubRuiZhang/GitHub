# python3
# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


# My solution
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        letter_times = {}
        times_letter = [[] for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] in letter_times:
                times_letter[letter_times[s[i]] - 1].remove(s[i])
                letter_times[s[i]] += 1
                times_letter[letter_times[s[i]] - 1].append(s[i])
            else:
                letter_times[s[i]] = 1
                times_letter[0].append(s[i])
        out = ''
        for i in range(len(s)):
            if len(times_letter[-i - 1]) > 0:
                for l in times_letter[-i - 1]:
                    out += l * (len(s) - i)
            if len(out) == len(s):
                break
        return out

