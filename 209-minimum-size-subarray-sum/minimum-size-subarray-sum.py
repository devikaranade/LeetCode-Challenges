class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = 0
        r = 0
        total = 0
        while r<len(nums):
            total+=nums[r]
            if total>=target:
                while total>=target:
                    min_len = min(min_len, r-l+1)
                    total-=nums[l]
                    l+=1  
            r+=1
        return min_len if min_len!=float('inf') else 0
                

                