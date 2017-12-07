# python3
# Given a positive 32-bit integer n,
# you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n
# and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

# Example 1:
# Input: 12
# Output: 21
# Example 2:
# Input: 21
# Output: -1


# My solution
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_str = list(str(n))
        index = -1
        for i in range(len(n_str) - 1)[::-1]:
            if n_str[i] < n_str[i + 1]:
                ind = i + 1
                for j in range(i + 2, len(n_str)):
                    if n_str[j] > n_str[i] and n_str[j] < n_str[ind]:
                        ind = j
                n_str[i], n_str[ind] = n_str[ind], n_str[i]
                res = [n_str[it] for it in range(i + 1, len(n_str))]
                res.sort()
                n_str = n_str[:i + 1] + res
                out = int(''.join(n_str))
                if out > 2147483647:
                    return -1
                else:
                    return out

        return -1

