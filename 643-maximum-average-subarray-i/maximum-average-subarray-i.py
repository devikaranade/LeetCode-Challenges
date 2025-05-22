class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range(k):
            total+=nums[i]
        
        ans = total
        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i-k]
            ans = max(ans, total)
        
        return ans/k