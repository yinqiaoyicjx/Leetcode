
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

if __name__ == "__main__":
    result = Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print result