class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_len = float('inf')
        end = 0
        res = 0
        while end<len(nums):
            res += nums[end]
            while res>=target:
                min_len = min(min_len, end-start+1)
                res-=nums[start]
                start+=1
            end+=1
        return min_len if min_len!=float('inf') else 0
