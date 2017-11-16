# python3
# Given a nested list of integers, implement an iterator to flatten it.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:
# Given the list [[1,1],2,[1,1]],

# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Given the list [1,[4,[6]]],

# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


# My solution
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.cur_pos = 0

    def flatten_list(self, l):
        out = []
        i = 0
        while i < len(l):
            if l[i].isInteger():
                out.append(l[i])
            else:
                new = self.flatten_list(l[i].getList())
                out.extend(new)
            i += 1
        return out

    def next(self):
        """
        :rtype: int
        """
        out = self.nestedList[self.cur_pos].getInteger()
        self.cur_pos += 1
        return out

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.cur_pos < len(self.nestedList) and not self.nestedList[self.cur_pos].isInteger():
            res = self.nestedList[:self.cur_pos]
            new = self.flatten_list(self.nestedList[self.cur_pos].getList())
            res.extend(new)
            res.extend(self.nestedList[self.cur_pos + 1:])
            self.nestedList = [it for it in res]

        if self.cur_pos < len(self.nestedList):
            return True
        else:
            return False








            # Your NestedIterator object will be instantiated and called as such:
            # i, v = NestedIterator(nestedList), []
            # while i.hasNext(): v.append(i.next())