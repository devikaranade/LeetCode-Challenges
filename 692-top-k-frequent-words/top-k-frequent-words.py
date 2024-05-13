class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for w,f in count.items():
            heappush(heap,(-f, w))
        heapify(heap)
        return [heappop(heap)[1] for _ in range (k)]