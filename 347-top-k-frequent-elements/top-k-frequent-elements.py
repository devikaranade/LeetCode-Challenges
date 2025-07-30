class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Counter = {1:3, 2:2, 3:1}
        #min_heap = [(-3:1),(-2:2)]
        c = Counter(nums)
        heap = []
        for key,val in c.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        l = []

        for i in heap:
            l.append(i[1])
        return l
