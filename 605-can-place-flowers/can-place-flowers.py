class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for cur in range(len(flowerbed)):
            if (flowerbed[cur]==0 
            and (cur==0 or flowerbed[cur-1]==0) 
            and (cur==len(flowerbed)-1 or flowerbed[cur+1]==0)):
                    n-=1
                    flowerbed[cur]=1
                    if n==0:
                        return True
        return n<=0