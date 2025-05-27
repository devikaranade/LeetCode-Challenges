class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        m = []
        for key,v in freq.items():
            heappush(m, (v,key))
            if len(m)>k:
                heappop(m)
        l = []
        for v,key in m:
            l.append(key)
        return l


