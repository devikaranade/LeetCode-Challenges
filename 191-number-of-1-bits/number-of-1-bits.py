class Solution:
    def hammingWeight(self, n: int) -> int:
        s = ""
        count = 0
        bin_n = bin(n)[2:]
        bin_string = str(bin_n)
        for c in bin_string:
            if c=='1':
                count+=1
        return count

        