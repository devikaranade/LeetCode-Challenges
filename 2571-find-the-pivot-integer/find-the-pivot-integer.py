class Solution:
    m = 1000
    arr = [0]*(m+1)

    def pivotInteger(self, n: int) -> int:
        if self.arr[1]==0:
            for i in range(1, self.m+1):
                sum_val = i * (i+1)//2
                j=1
                while j*j<sum_val:
                    j+=1
                self.arr[i]=j if j*j==sum_val else -1
        return self.arr[n]