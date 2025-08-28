class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            eucledian = -((x*x)+(y*y))
            heapq.heappush(heap, (eucledian, [x,y]))
            if len(heap)>k:
                heapq.heappop(heap)
        l = []
        for k,v in heap:
            l.append([v[0],v[1]])
        return l