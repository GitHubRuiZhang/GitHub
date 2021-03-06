# python3
# Given an Iterator class interface with methods: next() and hasNext(),
# design and implement a PeekingIterator that support the peek() operation
# -- it essentially peek() at the element that will be returned by the next call to next().

# Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

# Call next() gets you 1, the first element in the list.

# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

# You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

# Follow up: How would you extend your design to be generic and work with all types, not just integer?


# My solution
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.save = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.save != False:
            return self.save
        else:
            self.save = self.iterator.next()
            return self.save

    def next(self):
        """
        :rtype: int
        """
        if self.save == False:
            cur = self.peek()
        else:
            cur = self.save

        self.save = False
        return cur

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.save != False or self.iterator.hasNext():
            return True
        else:
            return False


            # Your PeekingIterator object will be instantiated and called as such:
            # iter = PeekingIterator(Iterator(nums))
            # while iter.hasNext():
            #     val = iter.peek()   # Get the next element but not advance the iterator.
            #     iter.next()         # Should return the same value as [val].