class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)

        def dfs(s):
            if not visited[s]:
                visited[s]=True
                for j in range(len(isConnected)):
                    if isConnected[j][s]:
                        dfs(j)
   
        res = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                res += 1
        return res

