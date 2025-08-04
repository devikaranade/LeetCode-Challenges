class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        lucky = []
        for k,v in c.items():
            if v==k:
                lucky.append(k)
        return max(lucky) if lucky else -1