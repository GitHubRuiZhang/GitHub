# python3
# Given a char array representing tasks CPU need to do.
# It contains capital letters A to Z where different letters represent different tasks.
# Tasks could be done without original order. Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks,
# there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].


# My solution
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        all_letters = set(tasks)
        letters_count = []
        for l in all_letters:
            letters_count.append([l, tasks.count(l)])
        letters_count = sorted(letters_count, key=lambda l: l[1])
        count_max = 0
        for i in range(len(letters_count)):
            if letters_count[-i - 1][1] == letters_count[-1][1]:
                count_max += 1
            else:
                break
        return max(len(tasks), (letters_count[-1][1] - 1) * (n + 1) + count_max)

# How to prove that we can always find that perfect order?

        out = []
        while letters_count:
            cur = letters_count.pop()
            if out.count(None) == 0:
                new_extend = [None for _ in range(n * (cur[1] - 1) + cur[1])]
                for i in range(cur[1]):
                    new_extend[i * (n + 1)] = cur[0]
                out.extend(new_extend)
            else:
                pre = -float('inf')
                i = 0
                while i < len(out) and cur[1] > 0:
                    if out[i] == None and i > pre + n:
                        out[i] = cur[0]
                        cur[1] -= 1
                        pre = i
                        i += n
                    else:
                        i += 1

                if cur[1] > 0:
                    new_extend = [None for _ in range(n * (cur[1] - 1) + cur[1])]
                    for i in range(cur[1]):
                        new_extend[i * (n + 1)] = cur[0]
                    if pre < 0:
                        out.extend(new_extend)
                    elif len(out) - pre - 1 < n:
                        out.extend([None for _ in range(pre + 1 + n - len(out))])
                        out.extend(new_extend)
                    else:
                        out.extend(new_extend)

        return len(out)


