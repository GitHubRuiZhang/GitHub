# python3
# Find the total area covered by two rectilinear rectangles in a 2D plane.

# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.


# My solution
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E > C or G < A or F > D or H < B:
            return (C-A)*(D-B) + (H-F )*(G-E)
        return  (C-A)*(D-B) + (H-F)*(G-E) - ((min(G,C)-max(A,E)) * (min(D,H)-max(B,F) ))