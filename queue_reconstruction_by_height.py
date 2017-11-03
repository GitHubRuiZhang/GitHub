# python3
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


# My solution
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) == 0:
            return []
        all_group = {}
        heights = []
        for i in range(len(people)):
            if people[i][0] in all_group:
                all_group[people[i][0]].append(people[i][1])
            else:
                all_group[people[i][0]] = [people[i][1]]
                heights.append(people[i][0])
        heights.sort()
        people_new = []
        for i in range(len(all_group[heights[-1]])):
            people_new.append([heights[-1], i])

        for i in range(len(heights) - 1):
            current_height = heights[-2 - i]
            all_group[current_height].sort()
            for j in range(len(all_group[current_height])):
                people_new.insert(all_group[current_height][j], [current_height, all_group[current_height][j]])

        return people_new
