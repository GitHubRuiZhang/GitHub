# python3
# Given two words (beginWord and endWord), and a dictionary's word list,
# find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.


# My solution
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        begin = set([beginWord])
        end = set([endWord])
        length = 2
        letters = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)
        wordList.discard(beginWord)
        try:
            wordList.remove(endWord)
        except:
            return 0

        while begin:
            new = set()
            for it in begin:
                for i in range(len(it)):
                    for l in letters:
                        res = it[:i] + l + it[i + 1:]
                        if res in end:
                            return length
                        if res in wordList:
                            new.add(res)

            begin = new
            if len(begin) > len(end):
                begin, end = end, begin

            wordList -= new
            length += 1

        return 0





