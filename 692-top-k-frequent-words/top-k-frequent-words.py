class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = {}
        l = []
        for word in words:
            if word not in h:
                h[word]=1
            else:
                h[word]+=1

        min_heap = []
        for key,val in h.items():
            heapq.heappush(min_heap,(-val, key))   
        
        for i in range(k):
            l.append(heapq.heappop(min_heap)[-1])
        return l
