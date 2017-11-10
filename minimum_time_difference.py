# python3
# Given a list of 24-hour clock time points in "Hour:Minutes" format,
# find the minimum minutes difference between any two time points in the list.

# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# he number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.


# My solution
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def transform(time):
            hourminute = time.split(":")
            return int(hourminute[0]) * 60 + int(hourminute[1])

        for i in range(len(timePoints)):
            timePoints[i] = transform(timePoints[i])

        out = 720
        timePoints.sort()

        for i in range(1, len(timePoints)):
            out = min(out, (timePoints[i] - timePoints[i - 1]))

        if timePoints[-1] > 720:
            out = min(out, 1440 + timePoints[0] - timePoints[-1])

        return out


