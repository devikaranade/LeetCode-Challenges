class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dir_ = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            while q:
                row, col = q.popleft()
                for r,c in dir_:
                    nr = row+r
                    nc = col+c
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]=="1":  
                        q.append((nr,nc))
                        grid[nr][nc]="0"
                
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    bfs(r,c)
                    count+=1
        return count
