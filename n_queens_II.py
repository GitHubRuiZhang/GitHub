# python3
# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.


# My solution
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def search(queens, ijdiff, ijsum, out):
            p = len(queens)
            if p == n:
                out += 1
                return out
            for q in range(n):
                if q not in queens and p - q not in ijdiff and p + q not in ijsum:
                    out = search(queens + [q], ijdiff + [p - q], ijsum + [p + q], out)
            return out

        return search([], [], [], 0)