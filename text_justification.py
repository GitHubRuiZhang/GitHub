# python3
# Given an array of words and a length L, format the text such that each line
# has exactly L characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words,
# the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.

# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.

# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.


# My solution
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i = 0
        r = 0
        r_length = 0
        out = [[]]
        while i < len(words):
            if r_length + len(words[i]) <= maxWidth:
                out[r].append(words[i])
                r_length += (len(words[i]) + 1)
            else:
                if len(out[r]) == 1:
                    out[r] = out[r][0] + ' ' * (maxWidth - len(out[r][0]))
                else:
                    count = (maxWidth - r_length + 1) // (len(out[r]) - 1)
                    res = maxWidth - r_length + 1 - count * (len(out[r]) - 1)
                    cur = ''
                    for j in range(len(out[r]) - 1):
                        cur += (out[r][j] + ' ')
                        cur += ' ' * count
                        if j < res:
                            cur += ' '
                    cur += out[r][j + 1]
                    out[r] = cur
                out.append([words[i]])
                r += 1
                r_length = (len(words[i]) + 1)
            i += 1
        cur = ''
        for it in out[r]:
            cur += it
            cur += ' '
        cur = cur[:len(cur) - 1]
        while len(cur) < maxWidth:
            cur += ' '
        out[r] = cur
        return out




