# python3
# Given N axis-aligned rectangles where N > 0,
# determine if they all together form an exact cover of a rectangular region.

# Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2].
# (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


# Example 1:

# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]

# Return true. All 5 rectangles together form an exact cover of a rectangular region.

# Example 2:

# rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]

# Return false. Because there is a gap between the two rectangular regions.

# Example 3:

# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]

# Return false. Because there is a gap in the top center.

# Example 4:

# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]

# Return false. Because two of the rectangles overlap with each other.


# Solution
class Solution:
    def save(self, it):
        if it in self.corners:
            self.corners[it] += 1
        else:
            self.corners[it] = 1

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        self.corners = {}
        l, b, r, t, area = float('inf'), float('inf'), -float('inf'), -float('inf'), 0

        for it in rectangles:
            l, b, r, t = min(l, it[0]), min(b, it[1]), max(r, it[2]), max(t, it[3])
            area += (it[2] - it[0]) * (it[3] - it[1])
            self.save((it[0], it[1]))
            self.save((it[2], it[3]))
            self.save((it[0], it[3]))
            self.save((it[2], it[1]))

        if area != (t - b) * (r - l):
            return False

        cur = [(l, b), (r, t), (l, t), (r, b)]
        for it in cur:
            if it not in self.corners or self.corners[it] != 1:
                return False
        for it in self.corners:
            if self.corners[it] % 2 and it not in cur:
                return False
        return True

