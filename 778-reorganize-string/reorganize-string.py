class Solution:
    def reorganizeString(self, s: str) -> str:
        map_s = Counter(s)
        max_el = 0
        
        for k,v in map_s.items():
            if v>max_el:
                max_el = v
                letter = k
        if max_el>(len(s)+1)//2:
            return ""
        
        ans = ['']*len(s)
        i = 0
        while map_s[letter]!=0:
            ans[i]=letter
            map_s[letter]-=1
            i+=2
        
        for char,count in map_s.items():
            while count>0:
                if i>=len(s):
                    i=1
                ans[i]=char
                count-=1
                i+=2
        return ''.join(ans)

        


            
        


