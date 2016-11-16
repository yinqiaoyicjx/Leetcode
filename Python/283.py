class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos=0
        for i in range(0,len(nums)):
            if nums[i]:
                nums[pos],nums[i]=nums[i],nums[pos]
                pos+=1
        print nums
t=Solution()
t.moveZeroes([0,1,0,3,12])


