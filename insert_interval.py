# python3
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].


# My solution
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        pre = intervals[0]
        i = 1
        while i < len(intervals):
            if intervals[i].start >= pre.start and intervals[i].end <= pre.end:
                intervals.pop(i)
            elif intervals[i].start >= pre.start and intervals[i].start <= pre.end and intervals[i].end > pre.end:
                cur = intervals[i].end
                intervals.pop(i - 1)
                intervals.pop(i - 1)
                pre = Interval(pre.start, cur)
                intervals.insert(i - 1, pre)
            else:
                pre = intervals[i]
                i += 1

        return intervals

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == [] or intervals[0].start > newInterval.start:
            intervals.insert(0, newInterval)
            return self.merge(intervals)
        i = 0
        while i < len(intervals) and intervals[i].start <= newInterval.start:
            i += 1
        intervals.insert(i, newInterval)
        return self.merge(intervals)
