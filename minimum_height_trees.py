# python3
# For a undirected graph with tree characteristics, we can choose any node as the root.
# The result graph is then a rooted tree.
# Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1.
# You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1:

# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3
# return [1]

# Example 2:

# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]

# Note:

# (1) According to the definition of tree on Wikipedia:
# “a tree is an undirected graph in which any two vertices are connected by exactly one path.
# In other words, any connected graph without simple cycles is a tree.”

# (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


# My solution
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # remove leaves
        adj = {}
        for it in edges:
            if it[0] in adj:
                adj[it[0]].add(it[1])
            else:
                adj[it[0]] = set([it[1]])
            if it[1] in adj:
                adj[it[1]].add(it[0])
            else:
                adj[it[1]] = set([it[0]])

        nodes = set(range(n))
        while len(nodes) > 2:
            visited = set()
            for it in adj.keys():
                if it not in visited and len(adj[it]) == 1:
                    nodes.remove(it)
                    cur = adj[it].pop()
                    adj[cur].remove(it)
                    visited.add(cur)
                    del adj[it]

        return list(nodes)

        # O(n**2)
        adj = [[0 for j in range(n)] for i in range(n)]
        for it in edges:
            adj[it[0]][it[1]] = 1
            adj[it[1]][it[0]] = 1
        print(adj)

        visited = [-1 for _ in range(n)]
        node_dis = {}

        def search1(node, dis):
            if visited[node] != -1:
                return
            if dis in node_dis:
                node_dis[dis].append(node)
            else:
                node_dis[dis] = [node]
            visited[node] = dis
            for i in range(n):
                if adj[node][i] == 1:
                    search1(i, dis + 1)
            return

        out = []
        out_dis = float('inf')
        i = 0
        while i < n:
            visited = [-1 for _ in range(n)]
            search1(i, 0)
            if max(visited) < out_dis:
                out_dis = max(visited)
                out = [i]
            elif max(visited) == out_dis:
                out.append(i)
            i += 1
        return out



