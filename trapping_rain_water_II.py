# python3
# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
# compute the volume of water it is able to trap after raining.

# Note:
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

# Example:

# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]

# Return 4.


# My solution
import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if heightMap == [] or heightMap == [[]]:
            return 0

        n = len(heightMap)
        m = len(heightMap[0])
        res = []
        visited = [[False for j in range(m)] for i in range(n)]

        for i in range(n):
            heapq.heappush(res, (heightMap[i][0], i, 0))
            heapq.heappush(res, (heightMap[i][m - 1], i, m - 1))
            visited[i][0] = True
            visited[i][m - 1] = True
        for j in range(1, m - 1):
            heapq.heappush(res, (heightMap[0][j], 0, j))
            heapq.heappush(res, (heightMap[n - 1][j], n - 1, j))
            visited[0][j] = True
            visited[n - 1][j] = True

        out = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while res:
            height, i, j = heapq.heappop(res)
            for it in directions:
                x = i + it[0]
                y = j + it[1]
                if 0 <= x <= n - 1 and 0 <= y <= m - 1 and not visited[x][y]:
                    out += max(0, height - heightMap[x][y])
                    heapq.heappush(res, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = True
        return out

