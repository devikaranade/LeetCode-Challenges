class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        in_deg = defaultdict(int)
        out_deg = defaultdict(int)
        for trusts, trusted in trust:
            in_deg[trusted]+=1
            out_deg[trusts]+=1
        
        for node, i in in_deg.items():
            if i==n-1 and out_deg[node]==0:
                return node
        return -1
