class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)
        rev = ''.join(reversed(n))
        return int(rev,2)