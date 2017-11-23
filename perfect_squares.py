# python3
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


# My solution
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        possible = [(i + 1) ** 2 for i in range(int(n ** 0.5))]
        print(possible)
        res = [n]
        out = 1
        while res:
            next_level = set()
            for cur in res:
                for j in range(len(possible)):
                    if cur - possible[j] == 0:
                        return out
                    elif cur - possible[j] > 0 and cur not in next_level:
                        next_level.add(cur - possible[j])
                    elif cur - possible[j] > 0:
                        continue
                    else:
                        continue
            res = [it for it in list(next_level)]
            out += 1

        return out


