class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        curr = 0
        max_len = 0
        for end in range(len(nums)):
            if nums[end]==0:
                curr+=1
            while curr>k:
                if nums[start]==0:
                    curr-=1
                start+=1
            max_len = max(max_len, end+1-start)
        return max_len