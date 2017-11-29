# python3
# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?


# My solution
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        def binary_search(citations, l, r):
            if l > r:
                return l
            mid = (l + r) // 2
            if citations[mid] < len(citations) - mid:
                return binary_search(citations, mid + 1, r)
            else:
                return binary_search(citations, l, mid - 1)

        if citations == []:
            return 0
        out = binary_search(citations, 0, len(citations) - 1)
        return len(citations) - out



