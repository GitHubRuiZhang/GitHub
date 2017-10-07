# python3
# You are given a data structure of employee information, which includes the employee's unique id,
# his importance value and his direct subordinates' id.

# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
# They have importance value 15, 10 and 5, respectively.
# Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]],
# and employee 3 has [3, 5, []].
# Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

# Now given the employee information of a company, and an employee id,
# you need to return the total importance value of this employee and all his subordinates.

# Example 1:
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11
# Explanation:
# Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
# They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.


# My solution:
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def __init__(self):
        self.total_value = 0
        self.visited = []

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.visited = [False for _ in range(len(employees))]
        self.search(employees, id)
        return self.total_value

    def search(self, employees, id):
        employee = employees[id - 1]
        if self.visited[id - 1] is True:
            return
        self.visited[id - 1] == True
        self.total_value += employee.importance
        for subordinate in employee.subordinates:
            self.search(employees, subordinate)
        return