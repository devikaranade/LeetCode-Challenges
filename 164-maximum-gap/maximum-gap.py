class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        minheap = []
        for i in nums:
            heapq.heappush(minheap, i)
        diff = float('-inf')
        while minheap:
            key = heapq.heappop(minheap)
            if minheap:
                diff = max(minheap[0]-key, diff)
        return diff
        