# python3
# Serialization is the process of converting a data structure or object into a sequence of bits so that
# it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed
# later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary search tree can be serialized to a string
# and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.


# My solution 1, too slow
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes = [[0, root]]
        out = []
        level = 0
        while nodes:
            cur = nodes.pop(0)
            if cur[1] is None:
                continue
            while cur[0] > len(out):
                out.append(str(None))
            out.append(str(cur[1].val))
            nodes.append([cur[0] * 2 + 1, cur[1].left])
            nodes.append([cur[0] * 2 + 2, cur[1].right])

        print(" ".join(out))
        return " ".join(out)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split()
        if nodes == []:
            return None
        all_nodes = []
        head = TreeNode(int(nodes[0]))
        all_nodes.append(head)
        for i in range(1, len(nodes)):
            new_node = None
            if nodes[i] != 'None':
                new_node = TreeNode(int(nodes[i]))
                if i % 2 == 1:
                    all_nodes[i // 2].left = new_node
                else:
                    all_nodes[i // 2 - 1].right = new_node

            all_nodes.append(new_node)

        return head


# My solution 2, fast
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes = [[0, root]]
        out = []
        level = 0
        while nodes:
            cur = nodes.pop(0)
            if cur[1] is None:
                continue
            out.append(str(cur[0]) + ' ' + str(cur[1].val))
            nodes.append([cur[0] * 2 + 1, cur[1].left])
            nodes.append([cur[0] * 2 + 2, cur[1].right])

        return " ".join(out)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split()
        if nodes == []:
            return None
        all_nodes = {}
        head = TreeNode(int(nodes[1]))
        all_nodes[int(nodes[0])] = head
        i = 2
        while i < len(nodes):
            new_node = TreeNode(int(nodes[i+1]))
            if int(nodes[i]) % 2 == 1:
                all_nodes[int(nodes[i]) // 2].left = new_node
            else:
                all_nodes[int(nodes[i]) // 2 - 1].right = new_node
            all_nodes[int(nodes[i])] = new_node
            i += 2
        return head



