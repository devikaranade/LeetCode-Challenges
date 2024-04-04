class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=res=0
        if len(s)==1:
            return 1
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
            else: 
                count-=1
            if count==-1:
                res+=1
                count+=1
        return res+count

        
        

        


        