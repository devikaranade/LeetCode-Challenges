class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        rev, x = 0, abs(x)
        while x:
            x,val = divmod(x,10)
            rev = rev*10 + val
            if rev>2**31-1:
                return 0 
        return sign*rev