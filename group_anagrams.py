# python3
# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.


# My solution
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        out = []
        out_dict = {}
        for i in range(len(strs)):
            cur = ''.join(sorted(strs[i]))
            if cur in out_dict:
                out[out_dict[cur]].append(strs[i])
            else:
                out.append([strs[i]])
                out_dict[cur] = len(out) - 1

        return out


