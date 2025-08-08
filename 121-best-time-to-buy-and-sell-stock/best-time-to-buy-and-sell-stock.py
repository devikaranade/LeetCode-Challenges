class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r<len(prices):
            diff = prices[r]-prices[l]
            if diff>max_profit:
                max_profit = diff
            if diff<0:
                l=r
            r+=1
        return max_profit