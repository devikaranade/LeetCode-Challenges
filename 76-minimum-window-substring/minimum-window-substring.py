class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minimum = float('inf')
        left, right = 0, 0
        t_map = defaultdict(int)
        for c in t:
            t_map[c]+=1
        ch = len(t)
        min_start=0
        while right<len(s):
            if t_map[s[right]]>0:
                ch-=1
            t_map[s[right]]-=1
            right+=1
            while ch==0:
                if right-left<minimum:
                    min_start=left
                    minimum=right-left
                t_map[s[left]]+=1
                if t_map[s[left]]>0:
                    ch+=1
                left+=1
        return s[min_start:min_start+minimum] if minimum!=float('inf') else ""





        