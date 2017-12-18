# python3
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
# You can assume that you can always reach the last index.


# My solution
class Solution(object):
    def search(self, nums, level, pre):
        # TLE
        if len(nums) - 1 in pre:
            return level
        while len(nums) - 1 not in pre:
            cur = []
            while pre:
                res = pre.pop()
                cur.extend([res + i + 1 for i in range(nums[res])])
            pre = set(cur)
            level += 1
        return level

        # TLE
        if len(nums) - 1 in pre:
            return level
        print(pre)
        cur = []
        while pre:
            res = pre.pop()
            cur.extend([res + i + 1 for i in range(nums[res])])
        pre = set(cur)
        level += 1
        return self.search(nums, level, pre)

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prestart, preend, count = 0, 1, 0
        while preend < len(nums):
            cur = min(nums[prestart] + prestart + 1, len(nums))
            while preend < cur:
                if nums[preend] + preend > nums[prestart] + prestart:
                    prestart = preend
                preend += 1
            count += 1
        return count

        # TLE
        return self.search(nums, 0, set([0]))

        # dp, TLE
        dp = [float('inf') for _ in range(len(nums))]
        dp[-1] = 0
        for i in reversed(range(len(nums) - 1)):
            j = nums[i]
            while j > 0:
                if i + j >= len(nums) - 1:
                    dp[i] = 1
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i + j])
                j -= 1

        return dp[0]
