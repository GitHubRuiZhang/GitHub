# python3
# Given two words (beginWord and endWord), and a dictionary's word list,
# find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.


# My solution
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        path_begin = {beginWord: [[beginWord]]}
        path_end = {endWord: [[endWord]]}
        letters = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)
        wordList.discard(beginWord)
        try:
            wordList.remove(endWord)
        except:
            return []

        out = []
        while path_begin:
            new = set()
            new_path = {}
            path_end_key = set(path_end.keys())
            for it in path_begin.keys():
                for i in range(len(it)):
                    for l in letters:
                        res = it[:i] + l + it[i + 1:]
                        if res in path_end_key:
                            for k1 in path_begin[it]:
                                for k2 in path_end[res]:
                                    out_res = k1 + k2[::-1]
                                    if out_res[0] == beginWord:
                                        out.append(out_res)
                                    else:
                                        out.append(out_res[::-1])

                        if res in wordList:
                            for k1 in path_begin[it]:
                                if res in new_path:
                                    new_path[res].append(k1 + [res])
                                else:
                                    new_path[res] = [k1 + [res]]
                            new.add(res)

            path_begin = new_path.copy()
            if len(path_begin) > len(path_end):
                path_begin, path_end = path_end, path_begin

            wordList -= new
            if out != []:
                return out

        return out

        # TLE
        path = [[beginWord]]
        letters = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)
        wordList.discard(beginWord)
        try:
            wordList.remove(endWord)
        except:
            return []

        out = []
        while path:
            new = set()
            new_path = []
            for it in path:
                for i in range(len(it[-1])):
                    for l in letters:
                        res = it[-1][:i] + l + it[-1][i + 1:]
                        if res == endWord:
                            out.append(it + [res])
                        if res in wordList:
                            new_path.append(it + [res])
                            new.add(res)

            path = new_path[:]
            wordList -= new
            if out != []:
                return out

        return out
