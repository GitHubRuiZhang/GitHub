# python3
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.


# My solution
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        step_n_1 = 2
        step_n_2 = 1
        for i in range(3, n + 1):
            save_num = step_n_1
            step_n_1 = step_n_1 + step_n_2
            step_n_2 = save_num

        return step_n_1