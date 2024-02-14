class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        op = 0
        for i in range(n):
            s = start + (i*2)
            nums.append(s)
        for i in nums:
            op^=i
        return op