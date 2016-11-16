class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=1
        n=len(nums)
        out=[]
        for i in range(0,n):
            out.append(p)
            p*=nums[i]
        p=1
        for i in range(n-1,-1,-1):
            out[i]*=p
            p*=nums[i]
        return out
