class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def to_delete(s, o, c):
            sb = []
            bal = 0
            for ch in s:
                if ch==o:
                    bal+=1
                if ch==c:
                    if bal==0:
                        continue
                    bal-=1
                sb.append(ch)
            return "".join(sb)
        s = to_delete(s, "(", ")")
        s = to_delete(s[::-1], ")", "(")
        return s[::-1]
                
        