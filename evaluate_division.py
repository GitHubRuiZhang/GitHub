# python3
# Equations are given in the format A / B = k, where A and B are variables represented as strings,
# and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist,
# return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
# where equations.size() == values.size(), and the values are positive. This represents the equations.
# Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# The input is always valid.
# You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


# My solution
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        def dfs(all_variables, num, den, visited):
            if den in all_variables[num]:
                return all_variables[num][den]
            else:
                visited[num] = True
                visited[den] = True
                keys = all_variables[num].keys()
                out = []
                for key in keys:
                    if visited[key] == False:
                        cur = dfs(all_variables, key, den, visited)
                        if cur is not None:
                            return all_variables[num][key] * cur
            return None

        all_variables = {}
        old_visited = {}
        for i in range(len(equations)):
            cur = equations[i]
            if cur[0] in all_variables:
                all_variables[cur[0]][cur[1]] = values[i]
            else:
                old_visited[cur[0]] = False
                all_variables[cur[0]] = {cur[1]: values[i]}

            if cur[1] in all_variables:
                all_variables[cur[1]][cur[0]] = 1 / values[i]
            else:
                old_visited[cur[1]] = False
                all_variables[cur[1]] = {cur[0]: 1 / values[i]}

        out = []
        print(all_variables)
        for item in queries:
            if item[0] in all_variables and item[1] in all_variables:
                visited = {}
                for key in all_variables.keys():
                    visited[key] = False
                cur = dfs(all_variables, item[0], item[1], visited)
                if cur is None:
                    out.append(-1.0)
                else:
                    out.append(cur)
            else:
                out.append(-1.0)

        return out




