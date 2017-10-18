# python3
# Given n points in the plane that are all pairwise distinct,
# a "boomerang" is a tuple of points (i, j, k)
# such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Find the number of boomerangs.
# You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

# Example:
# Input:
# [[0,0],[1,0],[2,0]]

# Output:
# 2

# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


# My solution
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        output = 0
        for point0 in points:
            distance_dict = {}
            for point1 in points:
                dis = (point0[0] - point1[0]) ** 2 + (point0[1] - point1[1]) ** 2
                if dis in distance_dict:
                    distance_dict[dis].append(point1)
                else:
                    distance_dict[dis] = [point1]
            for dis in distance_dict.items():
                if len(dis[1]) > 1:
                    output += len(dis[1]) * (len(dis[1]) - 1)

        return output
