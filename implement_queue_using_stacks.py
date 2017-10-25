# python3
# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size,
# and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque
# (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid
# (for example, no pop or peek operations will be called on an empty queue).


# My solution, i dont think this is a good solution
class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.current = False

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.queue == []



        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()


# My solution II
class MyQueueNode(object):
    def __init__(self, x):
        self.val = x
        self.chi = None


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.point_to_head = MyQueueNode('head')
        self.point_to_tail = MyQueueNode('tail')

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.point_to_head.chi == None:
            self.point_to_head.chi = MyQueueNode(x)
            self.point_to_tail.chi = self.point_to_head.chi
        else:
            self.point_to_tail.chi.chi = MyQueueNode(x)
            self.point_to_tail.chi = self.point_to_tail.chi.chi

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.point_to_head.chi == None:
            return None
        first_element = self.point_to_head.chi.val
        self.point_to_head.chi = self.point_to_head.chi.chi
        return first_element

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.point_to_head.chi == None:
            return None
        return self.point_to_head.chi.val

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.point_to_head.chi == None



        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()