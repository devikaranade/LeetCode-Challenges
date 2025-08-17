class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        s = set()

        for c in jewels:
            s.add(c)
        for i in stones:
            if i in s:
                count+=1
        return count
