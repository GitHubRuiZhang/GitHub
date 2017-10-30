# python3
# Write a function to find the longest common prefix string amongst an array of strings.


# My solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        out_pre = ''
        j = 1
        while j <= len(strs[0]):
            out_new = strs[0][:j]
            for i in range(len(strs)):
                if len(out_new) > len(strs[i]) or out_new != strs[i][:j]:
                    return out_pre
            out_pre = out_new
            j += 1
        return out_pre
