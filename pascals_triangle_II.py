# python3
# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?


# My solution
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        out = [[1] for _ in range(rowIndex+1)]
        for i in range(1, rowIndex+1):
            for j in range(1, i):
                out[i].append(out[i - 1][j - 1] + out[i - 1][j])
            out[i].append(1)

        return out[rowIndex]


# My solution
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        pre_row = [1]
        for i in range(1, rowIndex+1):
            new_row = [1]
            for j in range(1, i):
                new_row.append(pre_row[j - 1] + pre_row[j])
            new_row.append(1)
            pre_row = new_row

        return pre_row