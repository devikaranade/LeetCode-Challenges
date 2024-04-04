class Solution:
    def isHappy(self, n: int) -> bool:
        def get_num(n):
            sqsum = 0
            while n:
                digit = n%10
                n = n//10
                sq = digit*digit
                sqsum += sq
            return sqsum
        s = set()
        while n!=1 and n not in s:
            s.add(n)
            n = get_num(n)
        return n==1
        
            