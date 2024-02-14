class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        '''
        nums = [0, 2, 4, 6, 8]
        xor = 00^10 = 010 ^ 100 = 110^110=0000^1000=1000

        '''
        nums = []
        op = 0
        for i in range(n):
            s = start + (i*2)
            nums.append(s)
        for i in nums:
            op^=i
        return op
        