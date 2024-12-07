class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(grid,r,c):
            if (0<=r<m and 0<=c<n and grid[r][c]=="1"):
                grid[r][c]="0"
                dfs(grid,r-1,c)
                dfs(grid,r+1,c)
                dfs(grid,r,c+1)
                dfs(grid,r,c-1)
            return 

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    count+=1
        return count
        
        
                


