class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pSum = 0
        max_length = 0
        map_indices = {}
        for i, num in enumerate(nums):
            pSum += num

            if pSum==k:
                max_length = i + 1
            
            if pSum-k in map_indices:
                max_length = max(max_length, i-map_indices[pSum-k])
            
            if pSum not in map_indices:
                map_indices[pSum]=i
        return max_length