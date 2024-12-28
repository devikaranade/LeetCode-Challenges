class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0:1}
        total = 0
        max_length = 0
        for i, num in enumerate(nums):
            total+=num
            if total == k:
                max_length = i + 1
            if total-k in d:
                max_length = max(max_length, i-d[total-k])
            if total not in d:
                d[total]=i
        return max_length