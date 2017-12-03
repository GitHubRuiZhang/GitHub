# python3
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# For example,

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


# My solution
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequences = set([])
        out = []
        for i in range(len(s) - 9):
            if s[i:i + 10] in sequences:
                out.append(s[i:i + 10])
            else:
                sequences.add(s[i:i + 10])
        return list(set(out))

        # naive
        if len(s) < 10:
            return []
        out = []
        all_sub = []
        for i in range(len(s) - 9):
            if s[i:i + 10] not in out and s[i:i + 10] in all_sub:
                out.append(s[i:i + 10])
            elif s[i:i + 10] not in all_sub:
                all_sub.append(s[i:i + 10])
        return out


