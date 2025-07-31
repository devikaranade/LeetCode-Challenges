class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            xi = i[0]*i[0]
            yi = i[1]*i[1]
            eucledian_dist = -(xi+yi) # sqrt(10)
            heapq.heappush(heap, (eucledian_dist, i))
            if len(heap)>k:
                heapq.heappop(heap)
        l = []
        for k,v in heap:
            l.append([v[0],v[1]])
        return l


