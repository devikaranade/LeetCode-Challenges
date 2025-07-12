class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        dir_ = [(0,1),(1,0),(0,-1),(-1,0)]

        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        
        while q and fresh>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dir_:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
            time+=1
        return time if fresh==0 else -1
