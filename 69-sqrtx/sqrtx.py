class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left = 2
        right = x//2
        while left<=right:
            mid = left + (right - left)//2
            print(mid)
            if mid*mid==x:
                return mid
            elif (mid*mid)>x:
                right = mid-1
            else:
                left = mid+1
        return right

            
        
        