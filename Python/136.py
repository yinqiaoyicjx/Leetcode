class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y:x^y, nums)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(len(nums) == 1):
            return nums[0]
        for i in range(0,len(nums),2):
            if i == len(nums)-1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]


t=Solution()
print t.singleNumber([2,2,5,1,8,5,1])