# python3
# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
# The bricks have the same height but different width.
# You want to draw a vertical line from the top to the bottom and cross the least bricks.

# The brick wall is represented by a list of rows.
# Each row is a list of integers representing the width of each brick in this row from left to right.

# If your line go through the edge of a brick, then the brick is not considered as crossed.
# You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

# You cannot draw a line just along one of the two vertical edges of the wall,
# in which case the line will obviously cross no bricks.

# Example:
# Input:
# [[1,2,2,1],
#  [3,1,2],
#  [1,3,2],
#  [2,4],
#  [3,1,2],
#  [1,3,1,1]]
# Output: 2
# Explanation:

# Note:
# The width sum of bricks in different rows are the same and won't exceed INT_MAX.
# The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000].
# Total number of bricks of the wall won't exceed 20,000.


# My solution
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        all_edges = {}
        for i in range(len(wall)):
            for j in range(len(wall[i])):
                if j > 0:
                    wall[i][j] += wall[i][j - 1]
                if wall[i][j] in all_edges:
                    all_edges[wall[i][j]] += 1
                else:
                    all_edges[wall[i][j]] = 1

        all_edges_list = list(all_edges.keys())
        all_edges_list.sort()
        out = len(wall)
        for i in range(len(all_edges_list) - 1):
            out = min(out, len(wall) - all_edges[all_edges_list[i]])

        return out


