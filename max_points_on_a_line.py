# python3
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


# My solution
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import numpy as np


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        slope = {}
        out = 0
        for i in range(len(points)):
            slope = {'i': 1}
            same = 0
            for j in range(i + 1, len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same += 1
                elif points[j].x == points[i].x:
                    slope['i'] += 1
                else:
                    cur = (points[j].y - points[i].y) * np.longdouble(1) / (points[j].x - points[i].x)
                    if cur in slope:
                        slope[cur] += 1
                    else:
                        slope[cur] = 2
                # print(i, j, slope)
            for it in slope.keys():
                out = max(out, slope[it] + same)
        return out
