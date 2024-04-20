class Solution:
    def numSplits(self, s: str) -> int:
        if len(s)==1:
            return 0
        if len(s)==2:
            return 1
        count=0
        left = defaultdict(int)
        right = Counter(s) 
        for c in s:
            left[c]+=1 
            right[c]-=1 
            if right[c]==0:
                right.pop(c) 
            if len(left)==len(right):
                count+=1 
        return count