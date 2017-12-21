# python3
# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?


# My solution
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        out = 0
        left = [1 for i in range(n)]
        right = [1 for i in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        for i in range(n):
            out += max(left[i], right[i])

        return out



