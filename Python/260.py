import operator
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = reduce(operator.xor, nums)

        bit =  x_xor_y & -x_xor_y  #正数和它负值按位与的结果是原始最右边非0位的数字为1，其余位都为0

        result = [0, 0]
        for i in nums:
            result[bool(i & bit)] ^= i
        return result

class Solution2:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = 0
        for i in nums:
            x_xor_y ^= i

        bit = x_xor_y & ~(x_xor_y - 1)

        x = 0
        for i in nums:
            if i & bit:
                x ^= i

        return [x, x ^ x_xor_y]

t=Solution()
print t.singleNumber([1,2,1,5,3,2])
