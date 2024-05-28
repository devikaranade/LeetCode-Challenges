class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_p, p = 0, 0
        while i<len(prices) and j<len(prices):
            p = prices[j]-prices[i]
            max_p = max(p, max_p)
            if p<0:
                i=j
            j+=1
        return max_p