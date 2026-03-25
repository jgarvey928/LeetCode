class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_stocks = len(prices)
        i = 0
        total_made = 0
        stock_price = 0
        bought = False
        for i in range(num_stocks):
            price_today = prices[i]
            if i+1 <= num_stocks-1:
                price_tomorrow = prices[i+1]
            else:
                price_tomorrow = -1
            if price_today < price_tomorrow and not bought:
                stock_price = price_today
                bought = True
            if (price_tomorrow < price_today or i >= num_stocks-1) and bought:
                total_made = total_made + (price_today - stock_price)
                bought = False

        return total_made

            