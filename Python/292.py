class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n - 1) % 4 != 3:
            return True
        else:
            return False
s=Solution()
print s.canWinNim(5)