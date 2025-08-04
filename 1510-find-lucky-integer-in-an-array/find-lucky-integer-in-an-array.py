class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        lucky = -1
        for k,v in c.items():
            if v==k:
                lucky=max(lucky, k)
        return lucky