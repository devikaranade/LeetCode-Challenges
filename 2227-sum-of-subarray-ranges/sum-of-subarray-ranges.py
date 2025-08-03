class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for left in range(n):
            min_val = float('inf')
            max_val = float('-inf')
            for right in range(left, n):
                max_val = max(max_val, nums[right])
                min_val = min(min_val, nums[right])
                ans+=max_val-min_val
        return ans