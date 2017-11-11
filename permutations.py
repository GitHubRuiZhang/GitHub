# python3
# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


# My solution
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def search(num, nums):
            if len(nums) == 0:
                return [[num]]
            next_num = nums.pop()
            current = search(next_num, nums)
            out = []
            for i in range(len(current)):
                for j in range(len(current[i]) + 1):
                    new_item = [it for it in current[i]]
                    new_item.insert(j, num)
                    out.append(new_item)
            return out

        return search(nums.pop(), nums)




