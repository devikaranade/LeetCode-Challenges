class Solution:

    @lru_cache(maxsize=None)
    def rec(self, index, s)-> int:
        if index==len(s):
            return 1
        if s[index]=="0":
            return 0
        if index==len(s)-1:
            return 1
        answer = self.rec(index + 1, s)
        if int(s[index:index+2])<=26:
            answer+=self.rec(index+2,s)
        return answer

    def numDecodings(self, s: str) -> int:
        return self.rec(0,s)