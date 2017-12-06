# python3
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
# Thus, the itinerary must begin with JFK.

# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
# when read as a single string. For example,
# the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.


# My solution
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        all_items = {}
        for item in sorted(tickets)[::-1]:
            if item[0] in all_items:
                all_items[item[0]].append(item[1])
            else:
                all_items[item[0]] = [item[1]]

        out = []

        def search(pos):
            while pos in all_items and all_items[pos] != []:
                search(all_items[pos].pop())
            out.append(pos)

        search('JFK')
        return out[::-1]





