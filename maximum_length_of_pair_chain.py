# python3
# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
# Chain of pairs can be formed in this fashion.

# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
# You can select pairs in any order.

# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].


# My solution
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) == 1:
            return 1
        pairs = sorted(pairs, key=lambda pair: pair[0])
        count = [1 for _ in range(len(pairs))]
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and count[j] + 1 > count[i]:
                    count[i] = count[j] + 1

        return count[-1]

