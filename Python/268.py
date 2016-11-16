import operator
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        96%
        """
        l = len(nums)
        n = 0
        for i in range(l):
            n += i+1
            n -= nums[i]
        if  n == 0:
            return 0
        else:
            return n

class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums, \
                      reduce(operator.xor, xrange(len(nums) + 1)))