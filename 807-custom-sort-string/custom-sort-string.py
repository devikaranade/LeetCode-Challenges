class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map_order = {}
        for i in range(len(order)):
            map_order[order[i]]=i
        
        heap = []
        for ch in s:
            if ch in map_order:
                heapq.heappush(heap,(map_order[ch],ch))
            else:
                heapq.heappush(heap,(27,ch))
        res = ""
        while heap:
            res+=heapq.heappop(heap)[1]

        return res
            
