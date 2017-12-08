# python3
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


# My solution
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # better, use two pointer
        def search(nums, l, r, target):
            out = []
            lpre = None
            rpre = None
            while l < r:
                # remove duplicate
                if lpre == nums[l] and rpre == nums[r]:
                    l += 1
                    r -= 1
                    continue
                elif lpre == nums[l]:
                    l += 1
                    continue
                elif rpre == nums[l]:
                    r -= 1
                    continue
                # decide next pair
                if nums[l] + nums[r] == target:
                    res = [nums[l], nums[r]]
                    out.append(res)
                    lpre = nums[l]
                    rpre = nums[r]
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    rpre = nums[r]
                    r -= 1
                else:
                    lpre = nums[l]
                    l += 1
            return out

        out = []
        nums.sort()
        pre1 = None
        for i in range(len(nums) - 3):
            if pre1 == nums[i]:
                continue
            elif nums[i] > 0 and nums[i] > target:
                break
            pre1 = nums[i]
            pre2 = None
            for j in range(i + 1, len(nums) - 2):
                if nums[j] == pre2:
                    continue
                elif nums[j] > 0 and nums[i] + nums[j] > target:
                    break
                else:
                    res = search(nums, j + 1, len(nums) - 1, target - nums[i] - nums[j])
                    if res != []:
                        for it in res:
                            out.append([nums[i], nums[j], it[0], it[1]])
                pre2 = nums[j]

        return out


# naive
def twoSum(nums, j, target):
    if j > len(nums) - 2:
        return []
    elif j == len(nums) - 2:
        if nums[j] + nums[j + 1] == target:
            return [[nums[j], nums[j + 1]]]
        else:
            return []
    pre = None
    out = []
    for i in range(j, len(nums) - 1):
        if nums[i] == pre:
            continue
        if nums[i] > 0 and nums[i] > target:
            break
        pre = nums[i]
        pre2 = None
        for k in range(i + 1, len(nums)):
            if nums[i] + nums[k] == target and nums[k] != pre2:
                out.append([nums[i], nums[k]])
            elif nums[i] + nums[k] > target and nums[k] > 0:
                break
            pre2 = nums[k]
    return out


out = []
nums.sort()
pre1 = None
print(nums)
for i in range(len(nums) - 3):
    if nums[i] == pre1:
        continue
    elif nums[i] > 0 and nums[i] > target:
        break
    pre1 = nums[i]
    pre2 = None
    for j in range(i + 1, len(nums) - 2):
        if nums[j] == pre2:
            continue
        elif nums[j] > 0 and nums[i] + nums[j] > target:
            break
        else:
            res = twoSum(nums, j + 1, target - nums[i] - nums[j])
            if res != []:
                for it in res:
                    out.append([nums[i], nums[j], it[0], it[1]])
        pre2 = nums[j]

return out
