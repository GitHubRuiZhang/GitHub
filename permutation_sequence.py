# python3
# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.


# My solution
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # fast
        nums = [i + 1 for i in range(n)]
        count = 1
        for i in range(1, n):
            count *= i
        out = ''
        for i in range(1, n)[::-1]:
            out += str(nums[(k - 1) // count])
            nums.pop((k - 1) // count)
            k -= ((k - 1) // count) * count
            count /= i
        out += str(nums[0])
        return out

        # naive
        def search(nums):
            out = []
            if len(nums) == 1:
                return [str(nums[0])]
            for i in range(len(nums)):
                res = search(nums[:i] + nums[i + 1:])
                for it in res:
                    out.append(str(nums[i]) + it)
            return out

        out = search([i + 1 for i in range(n)])
        return out[k - 1]



