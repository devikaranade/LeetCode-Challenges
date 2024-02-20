class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = bin(num)[2:]
        steps=0
        for bit in n:
            if bit=="1":
                steps+=2
            else:
                steps+=1
        return steps-1