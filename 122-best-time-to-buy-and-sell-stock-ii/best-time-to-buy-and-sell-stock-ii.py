class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[right]>prices[right-1]:
                max_profit+=prices[right]-prices[right-1]
        return max_profit
