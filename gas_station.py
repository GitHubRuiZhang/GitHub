# python3
# There are N gas stations along a circular route,
# where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and
# it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.


# My solution
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        sub = float('inf')
        start = 0
        for i in range(len(gas)):
            res += gas[i] - cost[i]
            if res < sub:
                sub = res
                start = i + 1
        if res < 0:
            return -1
        else:
            return start % len(gas)

        # naive
        n = len(gas)
        for i in range(n):
            count = len(gas)
            res = gas[i]
            dec = False
            for j in range(i + 1, n):
                if cost[j - 1] > res:
                    dec = True
                    break
                else:
                    res -= cost[j - 1]
                    res += gas[j]
            if dec == True:
                continue
            if cost[n - 1] > res:
                continue
            else:
                res -= cost[n - 1]
                res += gas[0]
            for j in range(1, i + 1):
                if cost[j - 1] > res:
                    dec = True
                    break
                else:
                    res -= cost[j - 1]
                res += gas[j]
            if dec == True:
                continue
            else:
                return i
        return -1




