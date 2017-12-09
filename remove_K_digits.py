# python3
# Given a non-negative integer num represented as a string,
# remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


# My solution
class Solution(object):
    def search(self, out, num, count):
        if count == 0:
            out = min(out, int(num))
            return out
        for j in range(len(num)):
            out = min(out, self.search(out, num[:j] + num[j + 1:], count - 1))
        return out

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return '0'
        out = []
        target = len(num) - k
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        while len(out) > target:
            out.pop()
        return str(int(''.join(out)))

        # naive
        return str(self.search(out, num, k))


