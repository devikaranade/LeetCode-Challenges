class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        psum = 0

        for i, num in enumerate(nums):
            psum+=num
            if psum==k:
                count=i+1
            if psum-k in d:
                count = max(count, i-d[psum-k])
            if psum not in d:
                d[psum]=i
        return count
