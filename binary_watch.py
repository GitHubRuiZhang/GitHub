# python3
# A binary watch has 4 LEDs on the top which represent the hours (0-11),
# and the 6 LEDs on the bottom represent the minutes (0-59).

# Each LED represents a zero or one, with the least significant bit on the right.

# For example, the above binary watch reads "3:25".

# Given a non-negative integer n which represents the number of LEDs that are currently on,
# return all possible times the watch could represent.

# Example:

# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero,
# for example "10:2" is not valid, it should be "10:02".


# My solution
from itertools import combinations

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        output = []
        all_possible_list = list(combinations(range(10), num))
        for comb in all_possible_list:
            time_list = [0,0]
            for sub_time in comb:
                if sub_time <= 3:
                    time_list[0] += 2**(sub_time)
                else:
                    time_list[1] += 2**(sub_time - 4)
            if time_list[0] >= 12 or time_list[1] >= 60:
                continue
            time_str = str(time_list[0]) + ':'
            if time_list[1] < 10:
                time_str += ('0' + str(time_list[1]))
            else:
                time_str += str(time_list[1])
            output.append(time_str)
        return output
