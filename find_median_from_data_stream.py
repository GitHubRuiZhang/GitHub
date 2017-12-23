# python3
# Median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# Examples:
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2


# solution
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        l, r = self.data
        heapq.heappush(l, -heapq.heappushpop(r, num))
        if len(r) < len(l):
            heapq.heappush(r, -heapq.heappop(l))

    def findMedian(self):
        """
        :rtype: float
        """
        l, r = self.data
        if len(r) > len(l):
            return float(r[0])
        return (r[0] - l[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()