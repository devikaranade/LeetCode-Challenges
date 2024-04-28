class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        loc = [0]*1001
        for i,j,k in trips:
            loc[j]+=i
            loc[k]-=i

        for i in loc:
            capacity-=i
            if capacity<0:
                return False
        return True

            
        