class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x<0]
        rev, x = 0, abs(x)
        while x:
            mod = x%10
            x = x//10 
            rev = 10*rev + mod # 3 321
            if rev>2**31-1:
                return 0
        return sign*rev


        