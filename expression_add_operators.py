# python3
# Given a string that contains only digits 0-9 and a target value,
# return all possibilities to add binary operators (not unary) +, -, or *
# between the digits so they evaluate to the target value.

# Examples:
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []


# Solution
class Solution(object):
    def search(self, num, temp, cur, last):
        if not num:
            if cur == self.target:
                self.res.append(temp)
            return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 0 and num[0] != "0"):
                self.search(num[i:], temp + "+" + val, cur + int(val), int(val))
                self.search(num[i:], temp + "-" + val, cur - int(val), -int(val))
                self.search(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val))

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        self.target = target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                self.search(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return self.res
