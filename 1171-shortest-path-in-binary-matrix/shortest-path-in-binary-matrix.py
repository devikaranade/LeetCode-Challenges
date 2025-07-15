class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # shortest clear path
        # all visited path = 0
        # return -1 if no path exists 

        n = len(grid)
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1

        q = deque([(0,0,1)])
        dir_ = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        while q:
            r,c,dist = q.popleft()
            if r==n-1 and c==n-1:
                return dist
            for dr,dc in dir_:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<n and visited[nr][nc]!=True and grid[nr][nc]==0:
                    visited[nr][nc]=True
                    q.append((nr,nc,dist+1))
        return -1



        

        