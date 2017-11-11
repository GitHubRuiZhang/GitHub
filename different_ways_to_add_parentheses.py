# python3
# Given a string of numbers and operators,
# return all possible results from computing all the different possible ways to group numbers and operators.
# The valid operators are +, - and *.


# Example 1
# Input: "2-1-1".

# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]


# Example 2
# Input: "2*3-4*5"

# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]


# My solution
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        def operate(operation, nums1, nums2):
            out = []
            if operation == '+':
                for i in range(len(nums1)):
                    for j in range(len(nums2)):
                        out.append(nums1[i] + nums2[j])
            elif operation == '-':
                for i in range(len(nums1)):
                    for j in range(len(nums2)):
                        out.append(nums1[i] - nums2[j])
                        print(out)
            elif operation == '*':
                for i in range(len(nums1)):
                    for j in range(len(nums2)):
                        out.append(nums1[i] * nums2[j])
            return out

        def compute(operations, nums):
            if len(operations) == 0:
                return [nums[0]]
            elif len(operations) == 1:
                return operate(operations[0], [nums[0]], [nums[1]])
            out = []
            for i in range(len(operations)):
                left = compute(operations[:i], nums[:i + 1])
                right = compute(operations[i + 1:], nums[i + 1:])
                out.extend(operate(operations[i], left, right))
                print(left, right, operations[i])

            return out

        op = ['+', '-', '*']
        pre = 0
        operation = []
        nums = []
        for i in range(len(input)):
            if input[i] in op:
                operation.append(input[i])
                nums.append(int(input[pre:i]))
                pre = i + 1
        if operation == []:
            return [int(input)]
        nums.append(int(input[pre:]))

        return compute(operation, nums)

