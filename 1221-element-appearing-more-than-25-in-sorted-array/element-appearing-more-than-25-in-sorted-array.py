class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)
        p = n/4
        for k,v in c.items():
            if v>p:
                return k 