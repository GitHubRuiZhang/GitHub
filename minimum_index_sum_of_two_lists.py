# python3
# Suppose Andy and Doris want to choose a restaurant for dinner,
# and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.

# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.


# My solution, slow, I think it is because of the .index()
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sum_index = float('inf')
        for rest in list1:
            if rest in list2:
                si = list1.index(rest) + list2.index(rest)
                if si < sum_index:
                    choice = [rest]
                    sum_index = si
                elif si == sum_index:
                    choice.append(rest)

        return choice


# My solution
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sum_index = float('inf')
        list1_dict = {}
        choice = []
        for i in range(len(list1)):
            list1_dict[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in list1_dict:
                si = j + list1_dict[list2[j]]
                if si < sum_index:
                    sum_index = si
                    choice = [list2[j]]
                elif si == sum_index:
                    choice.append(list2[j])

        return choice