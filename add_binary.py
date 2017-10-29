# python3
# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".


# My solution
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        out = ''
        if len(a) > len(b):
            a, b = b, a
        pre = '0'
        for i in range(len(a)):
            cur = '0'
            if a[-i - 1] == '1' and b[-i - 1] == '1':
                cur = '0'
                if pre == '1':
                    cur = '1'
                pre = '1'
            elif a[-i - 1] == '0' and b[-i - 1] == '0':
                cur = '0'
                if pre == '1':
                    cur = '1'
                    pre = '0'
            else:
                cur = '1'
                if pre == '1':
                    cur = '0'
                    pre = '1'
            out = cur + out
        print(out, pre)
        if pre == '0':
            out = b[:(len(b) - len(a))] + out
        else:
            for i in range(len(b) - len(a)):
                if pre == '1':
                    if b[len(b) - len(a) - i - 1] == '1':
                        out = '0' + out
                        pre = '1'
                    else:
                        out = '1' + out
                        pre = '0'
                else:
                    out = b[:(len(b) - len(a) - i)] + out
                    break

        if pre == '1':
            out = '1' + out

        return out
