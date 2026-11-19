class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)

        return profit
