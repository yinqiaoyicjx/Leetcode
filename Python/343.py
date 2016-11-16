class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n-1
        if n == 4:
            return 4
        result=n%3
        if result == 1:
            return 4 * 3 ** ((n+1)/3-1)
        elif result == 2:
            return 2 * 3 ** ((n+1)/3-1)
        else:
            return 3 * 3 ** ((n+1)/3-1)
class Solution2(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1

        # integerBreak(n) = max(integerBreak(n - 2) * 2, integerBreak(n - 3) * 3)
        res = [0, 1, 2, 3]
        for i in xrange(4, n + 1):
            res[i % 4] = max(res[(i - 2) % 4] * 2, res[(i - 3) % 4] * 3)
        return res[n % 4]

s=Solution()
print s.integerBreak(2)
