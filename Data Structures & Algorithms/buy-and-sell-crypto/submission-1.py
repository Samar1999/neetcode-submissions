class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # buy_price = prices[0]
        # cur_profit = 0
        # max_profit = 0

        # for i in range(1, len(prices)):
        #     if prices[i] <= buy_price:
        #         buy_price = prices[i]
        #     else:
        #         cur_profit = prices[i] - buy_price
        #         max_profit = max(max_profit, cur_profit)
        
        # return max_profit

        #Using Sliding window approach
        l = 0
        r = 1
        cur_profit = 0
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                cur_profit = prices[r] - prices[l]
                max_profit = max(max_profit, cur_profit)
            else:
                l = r
            r += 1
        return max_profit