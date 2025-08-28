class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # h = {1:3, 2:2, 3:1}
        h = Counter(nums)
        heap = []
        for key,val in h.items():
            heapq.heappush(heap, (val, key))
            if len(heap)>k:
                heapq.heappop(heap)
        res = [] 
        for val, key in heap:
            res.append(key)
        return res