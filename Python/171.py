
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=len(s)
        sum=0
        for i in range(length):
            sum += (ord(s[i]) - ord('A')+1) * 26 ** (length-i-1)

        return sum
s=Solution()
print s.titleToNumber('AA')
