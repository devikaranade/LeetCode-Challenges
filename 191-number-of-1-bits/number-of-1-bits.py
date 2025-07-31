class Solution:
    def hammingWeight(self, n: int) -> int:
        # bit manipulation
        count = 0
        while n:
            count += n&1
            n>>=1
        return count


        # string 
        # s = ""
        # count = 0
        # bin_n = bin(n)[2:]
        
        # for c in bin_n:
        #     if c=='1':
        #         count+=1
        # return count 