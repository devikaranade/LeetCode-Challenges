class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        tmp = []
        for c in s:
            if c!='':
                tmp.append(c)
        return ' '.join(tmp[::-1])
                
            

        
        
        


        
        

        
        