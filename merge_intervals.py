# python3
# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# My solution
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        pre_start = intervals[0].start
        pre_end = intervals[0].end
        out = []
        for it in intervals:
            if it.start > pre_end:
                out.append(Interval(pre_start, pre_end))
                pre_start = it.start
                pre_end = it.end
            elif it.end > pre_end:
                pre_end = it.end
        out.append(Interval(pre_start, pre_end))
        return out
