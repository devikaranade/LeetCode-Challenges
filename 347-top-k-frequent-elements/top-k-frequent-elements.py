class Solution:
    def topKFrequent(self, nums: List[int], i: int) -> List[int]:
        h = Counter(nums)
        heap = []
        for k,v in h.items():
            heapq.heappush(heap, (v,k))
            if len(heap)>i:
                heapq.heappop(heap)
        res = []
        for v,k in heap:
            res.append(k)
        return res

