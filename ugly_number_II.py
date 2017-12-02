# python3
# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.


# My solution
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        pos = [0, 0, 0]
        out = [1]
        while len(out) < n:
            if out[pos[0]] * 2 <= out[pos[1]] * 3 and out[pos[0]] * 2 <= out[pos[2]] * 5:
                if out[pos[0]] * 2 != out[-1]:
                    out.append(out[pos[0]] * 2)
                pos[0] += 1
            elif out[pos[1]] * 3 <= out[pos[0]] * 2 and out[pos[1]] * 3 <= out[pos[2]] * 5:
                if out[pos[1]] * 3 != out[-1]:
                    out.append(out[pos[1]] * 3)
                pos[1] += 1
            elif out[pos[2]] * 5 <= out[pos[0]] * 2 and out[pos[2]] * 5 <= out[pos[1]] * 3:
                if out[pos[2]] * 5 != out[-1]:
                    out.append(out[pos[2]] * 5)
                pos[2] += 1
        # print(out)
        return out[-1]


