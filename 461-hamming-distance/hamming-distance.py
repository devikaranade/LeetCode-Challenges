class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x^y
        res=0
        while diff:
            res+=diff&1
            diff>>=1
        return res
            
        
        