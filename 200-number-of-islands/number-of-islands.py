class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) 
        n = len(grid[0]) 
        count = 0
        q = deque()
        dir_ = [(-1,0),(0,-1),(1,0),(0,1)]
        def bfs(r,c):
            q.append((r,c))
            while q:
                i,j = q.popleft()
                for dr,dc in dir_:
                    nr=i+dr
                    nc=j+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]=="1":
                        grid[nr][nc]="0"
                        q.append((nr,nc))

        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    bfs(r,c)
                    count+=1
        return count
