class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # s = "5F3Z-2e-9-w", k = 4
        # ans = ['W9E2',"-", "Z3F5"], count = 0

        n = len(s)
        count = 0
        ans = ['']
        for i in reversed(range(n)):
            if s[i]!="-":
                ans += s[i].upper()
                count+=1
                if count==k:
                    count=0
                    ans+="-"
        
        if len(ans)>0 and ans[len(ans)-1]=="-":
            ans=ans[:-1]
        ans = ans[::-1]
        result ="".join(ans)
        return result