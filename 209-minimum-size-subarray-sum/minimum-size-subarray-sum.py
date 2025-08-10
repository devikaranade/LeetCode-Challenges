class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        min_sub = float('inf')
        while r<len(nums):
            total += nums[r]
            while total>=target:
                min_sub = min(min_sub, r-l+1)
                total -= nums[l]
                l+=1
            r+=1
        return 0 if min_sub==float('inf') else min_sub