class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dir_ = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque()
        
        count = 0

        def bfs(i,j):
            
            
            q.append((i,j))
            while q:
                r,c = q.popleft()
                for dr,dc in dir_:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':
                        q.append((nr,nc))
                        grid[nr][nc]='0'



        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1':
                    bfs(r,c)
                    count+=1
        return count

