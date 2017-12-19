# python3
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.


# My solution
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # dp
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[True for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        for i in range(1, len(s2) + 1):
            dp[i][0] = dp[i - 1][0] and s2[i - 1] == s3[i - 1]
        for j in range(1, len(s1) + 1):
            dp[0][j] = dp[0][j - 1] and s1[j - 1] == s3[j - 1]
        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i - 1 + j]) or (
                        dp[i][j - 1] and s1[j - 1] == s3[i - 1 + j])
        return dp[-1][-1]

        # naive
        if len(s1) + len(s2) != len(s3):
            return False
        res = [[s1, s2]]
        for it in s3:
            exist = False
            new = []
            for i in range(len(res)):
                if res[i][0] != "" and res[i][0][0] == it:
                    new.append([res[i][0][1:], res[i][1]])
                    exist = True
                if res[i][1] != "" and res[i][1][0] == it:
                    new.append([res[i][0], res[i][1][1:]])
                    exist = True
            if exist == False:
                return False
            res = new[:]

        return True




