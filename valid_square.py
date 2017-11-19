# python3
# Given the coordinates of four points in 2D space, return whether the four points could construct a square.

# The coordinate (x,y) of a point is represented by an integer array with two integers.

# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# Note:

# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.


# My solution
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dis_1_to_2 = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        dis_1_to_3 = ((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
        dis_1_to_4 = ((p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2)
        dis_2_to_3 = ((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
        dis_2_to_4 = ((p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2)
        dis_3_to_4 = ((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2)
        res = sorted([dis_1_to_2, dis_1_to_3, dis_1_to_4, dis_2_to_3, dis_2_to_4, dis_3_to_4])
        print(res)
        if res[0] != res[3] or res[0] == res[4] or res[0] + res[1] != res[4]:
            return False
        return True

