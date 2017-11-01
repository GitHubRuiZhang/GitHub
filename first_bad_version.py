# python3
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.


# My solution
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n == 1:
            return 1
        i = 1
        j = n
        result_i = isBadVersion(1)
        result_j = isBadVersion(n)
        if result_i == True:
            return 1
        last_good = 1
        first_bad = n
        while True:
            print(i, j)
            result_i = isBadVersion(i)
            result_j = isBadVersion(j)
            if not result_i and result_j:
                last_good = max(last_good, i)
                first_bad = min(first_bad, j)
                if i == j - 1:
                    return j
                else:
                    j = (j + i) // 2
            elif not result_i and not result_j:
                last_good = max(i, j, last_good)
                i = last_good
                j = first_bad
            elif result_i and not result_j:
                i = last_good = max(last_good, j)
                j = first_bad = min(first_bad, i)
            elif result_i and result_j:
                i = last_good
                first_bad = min(first_bad, i, j)
