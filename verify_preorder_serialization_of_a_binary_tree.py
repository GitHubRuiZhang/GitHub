# python3
# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node,
# we record the node's value. If it is a null node, we record using a sentinel value such as #.

#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
# where # represents a null node.

# Given a string of comma separated values,
# verify whether it is a correct preorder traversal serialization of a binary tree.
# Find an algorithm without reconstructing the tree.

# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

# You may assume that the input format is always valid,
# for example it could never contain two consecutive commas such as "1,,3".

# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true

# Example 2:
# "1,#"
# Return false

# Example 3:
# "9,#,#,1"
# Return false

# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.


# My solution
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder_list = preorder.split(',')
        out = []
        for i in range(len(preorder_list)):
            out.append(preorder_list[i])
            while len(out) > 1 and out[-1] == '#' and out[-2] == '#':
                out.pop()
                out.pop()
                if len(out) == 0:
                    return False
                out.pop()
                out.append('#')

        print(out)
        if len(out) == 1 and out[0] == '#':
            return True
        else:
            return False
