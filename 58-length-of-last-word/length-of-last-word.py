class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split(" ")
        
        for i in range(len(sp)-1, -1, -1):
            if len(sp[i])>0:
                return len(sp[i])
        return 0
            
            
        