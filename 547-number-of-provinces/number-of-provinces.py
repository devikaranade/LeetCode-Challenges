class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited[node]=1     
            for neighbor in range(0, len(isConnected)):
                if isConnected[node][neighbor]==1 and not visited[neighbor]:
                    dfs(neighbor)
                                     
        total_provinces = 0
        visited = [0]*len(isConnected)
        for row in range(0, len(isConnected)):
            if not visited[row]:
                dfs(row)
                total_provinces+=1 
        return total_provinces
