# python3
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


# My solution
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        out = []

        def search(s, i, pre, count):
            if count == 4 and i < len(s):
                return
            elif count == 4:
                out.append(pre[:len(pre) - 1])
            j = 0
            while i + j < len(s) and j < 3:
                cur = s[i:i + j + 1]
                if int(cur) >= 256 or (len(cur) > 1 and cur[0] == '0'):
                    j += 1
                    continue
                new = pre + cur + '.'
                search(s, i + j + 1, new, count + 1)
                j += 1

        search(s, 0, '', 0)
        return out



