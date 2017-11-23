# python3
# Write a program to find the nth super ugly number.

# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
# For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
# is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.


# My solution
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        out = [1 for _ in range(n)]
        list_value = [1 for _ in range(len(primes))]
        list_index = [-1 for _ in range(len(primes))]
        k = 0
        while k < n:
            cur = min(list_value)
            out[k] = cur
            for i in range(len(list_value)):
                if cur == list_value[i]:
                    list_index[i] += 1
                    list_value[i] = out[list_index[i]] * primes[i]
            k += 1

        return out[-1]

