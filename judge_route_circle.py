# python3
# My solution, slow

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count = [0,0]
        for i in range(len(moves)):
            if moves[i] == 'U':
                count[0] += 1
            elif moves[i] == 'D':
                count[0] -= 1
            elif moves[i] == 'L':
                count[1] += 1
            else:
                count[1] -= 1
        if count[0] is 0 and count[1] is 0:
            return True
        else:
            return False