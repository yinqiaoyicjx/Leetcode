
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt=0
        res=[]
        nums.sort()
        l=len(nums)
        for i in range(l):
            if cnt == 0:
                cnt=1
            elif nums[i] == nums[i-1]:
                cnt+=1
            else:
                cnt = 1
            if cnt > l//3.0 and nums[i] not in res:
                res.append(nums[i])
                cnt = 0
        return res
    def majorityElement2(self, nums):
        """first:scan list and find 2 num
           second:check the num.count >len/3
        """

        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]

t=Solution()
print t.majorityElement([1])
