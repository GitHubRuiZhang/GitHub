# python3
# Given a List of words, return the words that
# can be typed using letters of alphabet on only
# one row's of American keyboard.

# Example
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]


# My solution
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set_line_i = set(
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'])
        set_line_ii = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'])
        set_line_iii = set(['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'])
        set_lines = [set_line_i, set_line_ii, set_line_iii]
        output = []
        for i in range(len(words)):
            for j in range(3):
                if words[i][0] in set_lines[j]:
                    set_find = j
            for j in range(1, len(words[i])):
                if words[i][j] not in set_lines[set_find]:
                    set_find = False
                    break
            if set_find is not False:
                output.append(words[i])

        return (output)


# Better solution
# 1. We do not need to write every letter in both lowercase and uppercase
# c.lower() can transform the letter into its lower case
# 2. use '<=', think about the meaning of '>'
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set_line_i = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        set_line_ii = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        set_line_iii = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        output = []
        for i in range(len(words)):
            word = set([it.lower() for it in words[i]])
            if word <= set_line_i or word <= set_line_ii or word <= set_line_iii:
                output.append(words[i])

        return (output)


# Most people use the solution below
# It is faster, I think the reason is you do not need to use 'append' and the 'for' loop
class Solution(object):
    def findWords(self, words):
        return [word for word in words if valid(word)]


fst = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
snd = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
thd = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])


def valid(word):
    word = set([c.lower() for c in word])
    return word <= fst or word <= snd or word <= thd
