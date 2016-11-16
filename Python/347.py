from collections import Counter, defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c=Counter(nums)
        return [i for i,j in c.most_common(k)]

from random import randint

class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1

        p = []
        for key, val in counts.iteritems():
            p.append((val, key))
        self.kthElement(p, k);

        result = []
        for i in xrange(k):
            result.append(p[i][1])
        return result


    def kthElement(self, nums, k):
        def PartitionAroundPivot(left, right, pivot_idx, nums):
            pivot_value = nums[pivot_idx][0]
            new_pivot_idx = left
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            for i in xrange(left, right):
                if nums[i][0] > pivot_value:
                    nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                    new_pivot_idx += 1

            nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
            return new_pivot_idx

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

s=Solution()
print s.topKFrequent([1,1,1,2,2,3],2)