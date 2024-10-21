class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            if i<0 or i==m or j<0 or j==n or grid[i][j]=='0':
                return
            grid[i][j]="0" #-1 represents visited
            dfs(i-1,j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1":
                    dfs(row, col)
                    counter+=1
                    
        return counter


        