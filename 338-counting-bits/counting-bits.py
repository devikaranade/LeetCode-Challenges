class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0,n+1):
            tmp = bin(i)[2:]
            count_ones = tmp.count('1')
            ans.append(count_ones)
        return ans
        

        