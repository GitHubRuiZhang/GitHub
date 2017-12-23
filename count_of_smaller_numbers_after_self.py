# python3
# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# Example:

# Given nums = [5, 2, 6, 1]

# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].


# Solution
class Solution(object):
    def sort(self, res):
        mid = len(res) / 2
        if mid:
            l, r = self.sort(res[:mid]), self.sort(res[mid:])
            for i in range(len(res))[::-1]:
                if not r or l and l[-1][1] > r[-1][1]:
                    self.out[l[-1][0]] += len(r)
                    res[i] = l.pop()
                else:
                    res[i] = r.pop()
        return res

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.out = [0 for _ in range(len(nums))]
        self.sort(list(enumerate(nums)))
        return self.out


