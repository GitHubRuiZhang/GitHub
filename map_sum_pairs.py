# python3
# Implement a MapSum class with insert, and sum methods.

# For the method insert, you'll be given a pair of (string, integer). The string represents the key
# and the integer represents the value. If the key already existed,
# then the original key-value pair will be overridden to the new one.

# For the method sum, you'll be given a string representing the prefix,
# and you need to return the sum of all the pairs' value whose key starts with the prefix.

# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5


# My solution
class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.all_keys = []
        self.str_to_int = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key not in self.str_to_int:
            self.all_keys.append(key)

        self.str_to_int[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        out_sum = 0
        for key_it in self.all_keys:
            if len(key_it) >= len(prefix) and prefix == key_it[:len(prefix)]:
                out_sum += self.str_to_int[key_it]
        return out_sum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


