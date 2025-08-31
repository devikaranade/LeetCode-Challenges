class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        start = end = 0
        total = sum(nums)
        max_len = -1
        diff = total - x
        if diff<0:
            return -1
        res = 0
        while end<len(nums):
            res += nums[end]
            
            while res>diff and start<=end:
                res-=nums[start]
                start+=1
            if res==diff:
                max_len = max(max_len, end-start+1)
            end+=1
            
        return len(nums)-max_len if max_len!=-1 else -1
