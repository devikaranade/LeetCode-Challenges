class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        count=0

        def dfs(r,c):
            if (r<0 or r>=m or c<0 or c>=n or grid[r][c]=='0' or (r,c) in visited):
                return
            visited.add((r,c))

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1' and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        return count