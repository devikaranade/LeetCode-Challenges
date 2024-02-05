class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''


        '''
        h={}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i]+=1
        
        min_heap = []
        l = []
        for key, val in h.items():
            heappush(min_heap, (val,key))
            if len(min_heap)>k:
                heappop(min_heap)

        for val,key in min_heap:
            l.append(key)
        return l
        
        
         


        