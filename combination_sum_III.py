# python3
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


# Example 1:

# Input: k = 3, n = 7

# Output:

# [[1,2,4]]

# Example 2:

# Input: k = 3, n = 9

# Output:

# [[1,2,6], [1,3,5], [2,3,4]]


# My solution
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def search(k, n, nums):
            if nums == []:
                return []
            if k == 1 and n in nums:
                return [[n]]
            elif k == 1:
                return []

            out = []
            for i in range(len(nums)):
                if nums[i] * k > n or i + k > len(nums):
                    break

                cur = search(k - 1, n - nums[i], nums[i + 1:])
                for item in cur:
                    out.append([nums[i]] + item)

            return out

        return search(k, n, [i + 1 for i in range(9)])


