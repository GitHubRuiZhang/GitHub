# python3

# Given an integer array with even length, where different numbers in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind.
# You need to distribute these candies equally in number to brother and sister.
# Return the maximum number of kinds of candies the sister could gain.

# Example:
# Input: candies = [1,1,2,2,3,3]
# Output: 3
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
# The sister has three different kinds of candies.

# Example:
# Input: candies = [1,1,2,3]
# Output: 2
# Explanation:
# Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
# The sister has two different kinds of candies, the brother has only one kind of candies.


# My solution: Fail
# I tried to maximize the kinds of candies that the brother owns, so I sort candies first, and only give the new kind
# of candy to the brother. The problem is on the conditions that I break the loop.
# When the sister has n//2 candies, it does not indicate that this is the best solution.
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies.sort()
        brother = []
        sister = []
        for i in range(len(candies)):
            if brother == []:
                brother.append(candies[i])
            elif len(brother) is len(candies) // 2:
                sister.extend(candies[i:])
                break
            elif len(sister) is len(candies) // 2:
                brother.extend(candies[i:])
                break
            elif brother[-1] is not candies[i]:
                brother.append(candies[i])
            else:
                sister.append(candies[i])
        return max(len(set(brother)), len(set(sister)))


# Solution
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)),len(candies)//2)


