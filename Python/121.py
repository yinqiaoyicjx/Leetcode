class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == "__main__":
    result = Solution().maxProfit([2,1,2,0,1])
    print result