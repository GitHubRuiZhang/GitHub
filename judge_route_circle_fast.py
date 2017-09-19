# python3
# other solutions

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # count() is faster?
        # return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

        # directly return is slower?
        ud = moves.count('U') == moves.count('D')
        lr = moves.count('L') == moves.count('R')
        return ud and lr