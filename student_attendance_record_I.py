# python3
# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:

# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't
# contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False


# My solution
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        out = True
        A = False
        L = 0
        for l in s:
            print(l, A, L)
            if A == True and l == 'A':
                return False
            elif l == 'A':
                A = True
            elif L == 0 and l == 'L':
                L += 1
            elif L == 1 and l == 'L':
                L += 1
            elif L == 2 and l == 'L':
                return False

            if L != 0 and l != 'L':
                L = 0

        return out