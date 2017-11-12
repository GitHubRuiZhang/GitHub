# python3
# Given a non-empty string containing an out-of-order English representation of digits 0-9,
# output the digits in ascending order.

# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits.
# That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"

# Output: "012"
# Example 2:
# Input: "fviefuro"

# Output: "45"


# My solution
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = []
        out.extend(['0' for _ in range(s.count('z'))])
        out.extend(['2' for _ in range(s.count('w'))])
        out.extend(['4' for _ in range(s.count('u'))])
        out.extend(['6' for _ in range(s.count('x'))])
        out.extend(['8' for _ in range(s.count('g'))])
        out.extend(['1' for _ in range(s.count('o') - s.count('z') - s.count('w') - s.count('u'))])
        out.extend(['3' for _ in range(s.count('h') - s.count('g'))])
        out.extend(['5' for _ in range(s.count('f') - s.count('u'))])
        out.extend(['7' for _ in range(s.count('s') - s.count('x'))])
        out.extend(['9' for _ in range(s.count('i') - s.count('x') - s.count('g') - s.count('f') + s.count('u'))])
        out.sort()
        return ''.join(out)

