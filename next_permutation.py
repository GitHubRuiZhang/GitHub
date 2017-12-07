# python3
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible,
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


# My solution
class Solution(object):
    def nextGreaterElement(self, nums):
        """
        :type n: int
        :rtype: int
        """
        n_str = nums
        index = -1
        for i in range(len(n_str) - 1)[::-1]:
            if n_str[i] < n_str[i + 1]:
                ind = i + 1
                for j in range(i + 2, len(n_str)):
                    if n_str[j] > n_str[i] and n_str[j] < n_str[ind]:
                        ind = j
                n_str[i], n_str[ind] = n_str[ind], n_str[i]
                res = [n_str[it] for it in range(i + 1, len(n_str))]
                res.sort()
                for j in range(i + 1, len(n_str)):
                    n_str[j] = res[j - i - 1]
                return n_str

        return nums.sort()

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.nextGreaterElement(nums)

